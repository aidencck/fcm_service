from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any, List

from app.models.user import User, SubscriptionStatus, BillingAddress
from app.services.billing_service import BillingService
from app.core.dependencies import get_current_user, get_admin_user
from app.infrastructure.cache.redis import RedisClient
from app.core.config.billing import BillingRule

router = APIRouter()

def get_billing_service(redis_client: RedisClient = Depends()) -> BillingService:
    return BillingService(redis_client)

@router.get("/me/usage")
async def get_my_usage(
    current_user: User = Depends(get_current_user),
    billing_service: BillingService = Depends(get_billing_service)
) -> Dict[str, Any]:
    """获取当前用户的API使用情况"""
    return billing_service.check_api_usage(current_user)

@router.get("/me/usage/history")
async def get_my_usage_history(
    days: int = 30,
    current_user: User = Depends(get_current_user),
    billing_service: BillingService = Depends(get_billing_service)
) -> Dict[str, Any]:
    """获取当前用户的使用历史"""
    if days < 1 or days > 365:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Days parameter must be between 1 and 365"
        )
    return billing_service.get_usage_history(current_user, days)

@router.get("/me/subscription")
async def get_my_subscription(
    current_user: User = Depends(get_current_user),
    billing_service: BillingService = Depends(get_billing_service)
) -> Dict[str, Any]:
    """获取当前用户的订阅信息"""
    return billing_service.check_subscription(current_user)

@router.post("/me/subscription/upgrade")
async def upgrade_subscription(
    tier: str,
    payment_method: str,
    billing_address: BillingAddress,
    current_user: User = Depends(get_current_user),
    billing_service: BillingService = Depends(get_billing_service)
) -> Dict[str, Any]:
    """升级订阅套餐"""
    if not billing_service.update_subscription(
        current_user,
        tier,
        payment_method,
        billing_address.dict()
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid subscription tier"
        )
    return {"message": "Subscription upgraded successfully"}

@router.post("/me/subscription/cancel")
async def cancel_subscription(
    current_user: User = Depends(get_current_user),
    billing_service: BillingService = Depends(get_billing_service)
) -> Dict[str, Any]:
    """取消订阅"""
    if not billing_service.cancel_subscription(current_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Subscription is already cancelled"
        )
    return {"message": "Subscription cancelled successfully"}

# Admin routes
@router.get("/admin/rules", dependencies=[Depends(get_admin_user)])
async def get_billing_rules(
    billing_service: BillingService = Depends(get_billing_service)
) -> Dict[str, BillingRule]:
    """获取所有计费规则（管理员）"""
    return billing_service.billing_config.get_all_rules()

@router.put("/admin/rules/{tier}", dependencies=[Depends(get_admin_user)])
async def update_billing_rule(
    tier: str,
    rule: BillingRule,
    billing_service: BillingService = Depends(get_billing_service)
) -> Dict[str, Any]:
    """更新计费规则（管理员）"""
    if not billing_service.billing_config.update_rule(tier, rule):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid subscription tier"
        )
    return {"message": "Billing rule updated successfully"} 