from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List
from ..models.user import User, SubscriptionStatus, SubscriptionHistory
from ..config.billing_config import BillingConfig, BillingRule
from ..utils.redis_client import RedisClient
import logging

logger = logging.getLogger(__name__)

class BillingService:
    def __init__(self, redis_client: RedisClient):
        self.redis = redis_client
        self.billing_config = BillingConfig()
        
    def _get_daily_key(self, user_id: str) -> str:
        today = datetime.now().strftime("%Y%m%d")
        return f"api:usage:{user_id}:daily:{today}"
        
    def _get_monthly_key(self, user_id: str) -> str:
        month = datetime.now().strftime("%Y%m")
        return f"api:usage:{user_id}:monthly:{month}"
        
    def check_subscription(self, user: User) -> Dict[str, Any]:
        """检查用户订阅状态"""
        now = datetime.now()
        is_expired = (
            user.subscription_end_date and 
            user.subscription_end_date < now
        )
        
        if is_expired and user.subscription_status != SubscriptionStatus.EXPIRED:
            user.subscription_status = SubscriptionStatus.EXPIRED
            logger.info(f"User {user.id} subscription expired")
            
        return {
            "status": user.subscription_status,
            "tier": user.subscription_tier,
            "start_date": user.subscription_start_date,
            "end_date": user.subscription_end_date,
            "is_active": user.subscription_status == SubscriptionStatus.ACTIVE,
            "is_trial": user.subscription_status == SubscriptionStatus.TRIAL,
            "is_expired": user.subscription_status == SubscriptionStatus.EXPIRED
        }
        
    def check_api_usage(self, user: User) -> Dict[str, Any]:
        """检查API使用情况"""
        daily_key = self._get_daily_key(user.id)
        monthly_key = self._get_monthly_key(user.id)
        
        daily_usage = self.redis.get_counter(daily_key) or 0
        monthly_usage = self.redis.get_counter(monthly_key) or 0
        
        rule = self.billing_config.get_rule(user.subscription_tier)
        if not rule:
            return {
                "error": "Invalid subscription tier",
                "daily_usage": daily_usage,
                "monthly_usage": monthly_usage
            }
            
        return {
            "daily_usage": daily_usage,
            "monthly_usage": monthly_usage,
            "daily_remaining": max(0, rule.daily_limit - daily_usage),
            "monthly_remaining": max(0, rule.monthly_limit - monthly_usage),
            "is_daily_exceeded": daily_usage >= rule.daily_limit,
            "is_monthly_exceeded": monthly_usage >= rule.monthly_limit,
            "daily_limit": rule.daily_limit,
            "monthly_limit": rule.monthly_limit,
            "price_per_request": rule.price_per_request
        }
        
    def increment_api_usage(self, user: User) -> bool:
        """增加API使用计数"""
        daily_key = self._get_daily_key(user.id)
        monthly_key = self._get_monthly_key(user.id)
        
        # 设置每日计数过期时间为2天
        self.redis.set_expire(daily_key, 172800)
        # 设置每月计数过期时间为62天
        self.redis.set_expire(monthly_key, 5356800)
        
        return (
            self.redis.increment_counter(daily_key) and
            self.redis.increment_counter(monthly_key)
        )
        
    def get_usage_history(self, user: User, days: int = 30) -> Dict[str, Any]:
        """获取使用历史"""
        history = {}
        today = datetime.now()
        
        for i in range(days):
            date = today - timedelta(days=i)
            date_str = date.strftime("%Y%m%d")
            key = f"api:usage:{user.id}:daily:{date_str}"
            usage = self.redis.get_counter(key) or 0
            history[date_str] = usage
            
        return history
        
    def update_subscription(
        self,
        user: User,
        new_tier: str,
        payment_method: Optional[str] = None,
        billing_address: Optional[Dict] = None
    ) -> bool:
        """更新用户订阅"""
        rule = self.billing_config.get_rule(new_tier)
        if not rule:
            return False
            
        # 记录历史
        history = SubscriptionHistory(
            tier=user.subscription_tier,
            status=user.subscription_status,
            start_date=user.subscription_start_date,
            end_date=datetime.now(),
            payment_method=user.payment_method,
            billing_address=user.billing_address
        )
        user.subscription_history.append(history)
        
        # 更新订阅信息
        user.subscription_tier = new_tier
        user.subscription_status = SubscriptionStatus.ACTIVE
        user.subscription_start_date = datetime.now()
        user.subscription_end_date = None
        if payment_method:
            user.payment_method = payment_method
        if billing_address:
            user.billing_address = billing_address
            
        return True
        
    def cancel_subscription(self, user: User) -> bool:
        """取消订阅"""
        if user.subscription_status == SubscriptionStatus.CANCELLED:
            return False
            
        user.subscription_status = SubscriptionStatus.CANCELLED
        user.subscription_end_date = datetime.now()
        return True 