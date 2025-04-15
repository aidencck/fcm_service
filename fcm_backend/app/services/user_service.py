import firebase_admin
from firebase_admin import auth
from typing import Optional, Dict
import uuid
import logging
from ..config.settings import settings
from ..utils.redis_client import RedisClient
from ..config.redis_config import REDIS_CONFIG

logger = logging.getLogger(__name__)

class UserService:
    def __init__(self):
        if not firebase_admin._apps:
            cred = firebase_admin.credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
            firebase_admin.initialize_app(cred)
        self.redis_client = RedisClient(**REDIS_CONFIG)
        self.cache_prefix = "user:"
        self.cache_expire = 3600  # 1小时过期

    async def create_user(self, platform: str, app_id: str, device_info: Optional[Dict] = None) -> str:
        """
        Create a new Firebase user and return the UID
        Args:
            platform: The platform (web, android, ios)
            app_id: The application identifier
            device_info: Optional device information
        Returns:
            str: The Firebase user UID
        """
        try:
            # Generate a unique identifier for the user
            unique_id = str(uuid.uuid4())
            
            # Create custom claims for the user
            custom_claims = {
                "platform": platform,
                "app_id": app_id,
                "device_info": device_info or {}
            }

            # Create the user in Firebase Auth
            user = auth.create_user(
                uid=unique_id,
                display_name=f"{platform}_{app_id}",
                disabled=False
            )

            # Set custom claims
            auth.set_custom_user_claims(user.uid, custom_claims)

            logger.info(f"Created new user with UID: {user.uid} for platform: {platform}, app_id: {app_id}")

            # 创建用户信息字典
            user_info = {
                "user_id": user.uid,
                "platform": platform,
                "app_id": app_id,
                "device_info": device_info
            }
            
            # 设置缓存
            cache_key = f"{self.cache_prefix}{user.uid}"
            self.redis_client.set(cache_key, user_info, self.cache_expire)
            
            return user.uid

        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            raise

    async def get_user_info(self, user_id: str) -> Dict:
        """
        Get user information from Firebase Auth
        Args:
            user_id: The Firebase user UID
        Returns:
            Dict: User information including custom claims
        """
        try:
            # 先尝试从缓存获取
            cache_key = f"{self.cache_prefix}{user_id}"
            user_info = self.redis_client.get(cache_key)
            
            if user_info:
                logging.info(f"Cache hit for user {user_id}")
                return user_info
            
            # 缓存未命中，从Firebase获取
            logging.info(f"Cache miss for user {user_id}, fetching from Firebase")
            user_info = await self._get_user_from_firebase(user_id)
            
            if user_info:
                # 存入缓存
                self.redis_client.set(cache_key, user_info, self.cache_expire)
            
            return user_info
        except Exception as e:
            logger.error(f"Error getting user info: {str(e)}")
            raise

    async def update_user_device_info(self, user_id: str, device_info: Dict) -> bool:
        """
        Update user's device information
        Args:
            user_id: The Firebase user UID
            device_info: New device information
        Returns:
            bool: True if successful
        """
        try:
            # 更新Firebase
            success = await self._update_firebase_device_info(user_id, device_info)
            
            if success:
                # 删除缓存，强制下次重新获取
                cache_key = f"{self.cache_prefix}{user_id}"
                self.redis_client.delete(cache_key)
                
                # 更新缓存中的设备信息
                user_info = await self._get_user_from_firebase(user_id)
                if user_info:
                    self.redis_client.set(cache_key, user_info, self.cache_expire)
            
            return success
        except Exception as e:
            logger.error(f"Error updating device info: {str(e)}")
            raise

    async def _get_user_from_firebase(self, user_id: str) -> Dict:
        """
        从Firebase获取用户信息
        """
        try:
            user = auth.get_user(user_id)
            custom_claims = auth.get_custom_user_claims(user_id)
            
            return {
                "uid": user.uid,
                "email": user.email,
                "display_name": user.display_name,
                "platform": custom_claims.get("platform"),
                "app_id": custom_claims.get("app_id"),
                "device_info": custom_claims.get("device_info", {}),
                "created_at": user.user_metadata.creation_timestamp,
                "last_sign_in": user.user_metadata.last_sign_in_timestamp
            }
        except Exception as e:
            logger.error(f"Error getting user info from Firebase: {str(e)}")
            raise

    async def _update_firebase_device_info(self, user_id: str, device_info: Dict) -> bool:
        """
        更新Firebase中的设备信息
        """
        try:
            # Get current custom claims
            current_claims = auth.get_custom_user_claims(user_id)
            
            # Update device info
            current_claims["device_info"] = device_info
            
            # Set updated claims
            auth.set_custom_user_claims(user_id, current_claims)
            
            logger.info(f"Updated device info for user: {user_id}")
            return True
        except Exception as e:
            logger.error(f"Error updating device info in Firebase: {str(e)}")
            return False 