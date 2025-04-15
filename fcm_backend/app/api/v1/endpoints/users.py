from fastapi import APIRouter, HTTPException, Depends, status
from typing import Dict, Any, List
from sqlalchemy.orm import Session

from app.models.user import CreateUserRequest, UserResponse, UpdateDeviceInfoRequest
from app.services.user_service import UserService
from app.core.dependencies import get_current_user
from app.utils.redis_init import RedisClient

router = APIRouter()
user_service = UserService()

def get_user_service(redis_client: RedisClient = Depends()) -> UserService:
    return UserService(redis_client)

@router.post("/create", response_model=UserResponse)
async def create_user(request: CreateUserRequest, db: Session = Depends(get_db)):
    """
    Create a new Firebase user
    """
    try:
        # Convert device info to dict if present
        device_info = request.device_info.dict() if request.device_info else None
        
        # Create user in Firebase
        user_id = await user_service.create_user(
            platform=request.platform,
            app_id=request.app_id,
            device_info=device_info
        )
        
        # Get user info
        user_info = await user_service.get_user_info(user_id)
        return UserResponse(**user_info)
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    """
    Get user information
    """
    try:
        user_info = await user_service.get_user_info(user_id)
        return UserResponse(**user_info)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{user_id}/device-info", response_model=bool)
async def update_device_info(user_id: str, request: UpdateDeviceInfoRequest):
    """
    Update user's device information
    """
    try:
        success = await user_service.update_user_device_info(
            user_id=user_id,
            device_info=request.device_info.dict()
        )
        if not success:
            raise HTTPException(status_code=400, detail="Failed to update device info")
        return success
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

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
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Days parameter must be between 1 and 365"
        )
    return user_service.get_usage_history(current_user, days) 