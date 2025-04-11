from fastapi import APIRouter, HTTPException
from ...models.user import CreateUserRequest, UserResponse, UpdateDeviceInfoRequest
from ...services.user_service import UserService
from typing import Dict

router = APIRouter()
user_service = UserService()

@router.post("/create", response_model=UserResponse)
async def create_user(request: CreateUserRequest):
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