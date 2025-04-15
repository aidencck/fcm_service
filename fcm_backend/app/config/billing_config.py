from typing import Dict, Any, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta

class BillingRule(BaseModel):
    name: str
    daily_limit: int
    monthly_limit: int
    price_per_request: float
    description: Optional[str] = None
    is_active: bool = True
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class BillingConfig:
    def __init__(self):
        self.rules: Dict[str, BillingRule] = {}
        self._load_default_rules()
        
    def _load_default_rules(self):
        """加载默认计费规则"""
        self.rules = {
            "free": BillingRule(
                name="Free Tier",
                daily_limit=100,
                monthly_limit=3000,
                price_per_request=0.0,
                description="Basic access with limited features"
            ),
            "basic": BillingRule(
                name="Basic Tier",
                daily_limit=1000,
                monthly_limit=30000,
                price_per_request=0.01,
                description="Standard access with all features"
            ),
            "premium": BillingRule(
                name="Premium Tier",
                daily_limit=5000,
                monthly_limit=150000,
                price_per_request=0.005,
                description="Enhanced access with priority support"
            )
        }
        
    def get_rule(self, tier: str) -> Optional[BillingRule]:
        """获取指定套餐的计费规则"""
        return self.rules.get(tier)
        
    def update_rule(self, tier: str, rule: BillingRule) -> bool:
        """更新计费规则"""
        if tier not in self.rules:
            return False
        rule.updated_at = datetime.now()
        self.rules[tier] = rule
        return True
        
    def calculate_cost(self, tier: str, requests: int) -> float:
        """计算指定套餐的请求成本"""
        rule = self.get_rule(tier)
        if not rule:
            return 0.0
        return requests * rule.price_per_request
        
    def get_limits(self, tier: str) -> Dict[str, int]:
        """获取指定套餐的限制"""
        rule = self.get_rule(tier)
        if not rule:
            return {"daily_limit": 0, "monthly_limit": 0}
        return {
            "daily_limit": rule.daily_limit,
            "monthly_limit": rule.monthly_limit
        }
        
    def get_all_rules(self) -> Dict[str, BillingRule]:
        """获取所有计费规则"""
        return self.rules 