from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any
from ..models.user import User
from ..services.user_service import UserService
from ..utils.redis_client import RedisClient
from ..utils.security import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

def get_user_service(redis_client: RedisClient = Depends()) -> UserService:
    return UserService(redis_client)

@router.get("/me/usage")
async def get_my_usage(
    current_user: User = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
) -> Dict[str, Any]:
    """获取当前用户的API使用情况"""
    return user_service.check_api_usage(current_user)

@router.get("/me/usage/history")
async def get_my_usage_history(
    days: int = 30,
    current_user: User = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
) -> Dict[str, Any]:
    """获取当前用户的使用历史"""
    if days < 1 or days > 365:
        raise HTTPException(
            status_code=400,
            detail="Days parameter must be between 1 and 365"
        )
    return user_service.get_usage_history(current_user, days) 