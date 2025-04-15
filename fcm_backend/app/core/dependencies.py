from typing import Optional, Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer
from firebase_admin import firestore
from jose import JWTError, jwt
from app.config.settings import settings
from app.models.user import User
from app.services.user_service import UserService

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def get_db() -> Generator:
    """
    获取 Firebase 数据库实例
    """
    try:
        db = firestore.client()
        yield db
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database connection error: {str(e)}"
        )

async def get_current_user(
    api_key: Optional[str] = Depends(api_key_header),
    user_service: UserService = Depends(UserService),
    db = Depends(get_db)
) -> User:
    """
    通过 API Key 获取当前用户
    """
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key is missing"
        )
    
    try:
        # 从缓存或数据库获取用户信息
        user_info = await user_service.get_user_info(api_key)
        if not user_info:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid API Key"
            )
        
        # 检查用户是否活跃
        if not user_info.get("is_active", True):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User is not active"
            )
        
        # 转换为 User 模型
        user = User(
            id=user_info["user_id"],
            email=user_info.get("email", ""),
            subscription_tier=user_info.get("subscription_tier", "free"),
            subscription_status=user_info.get("subscription_status", "trial"),
            subscription_start_date=user_info.get("subscription_start_date"),
            subscription_end_date=user_info.get("subscription_end_date"),
            payment_method=user_info.get("payment_method"),
            billing_address=user_info.get("billing_address"),
            subscription_history=user_info.get("subscription_history", []),
            api_key=api_key,
            is_active=user_info.get("is_active", True)
        )
        
        return user
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    获取当前活跃用户
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is not active"
        )
    return current_user
