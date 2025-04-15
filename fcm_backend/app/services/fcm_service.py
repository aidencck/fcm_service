import firebase_admin
from firebase_admin import credentials, messaging
from typing import List, Optional, Dict, Any
from datetime import datetime
from ..models.fcm import FCMToken, FCMMessage, MessageTarget, MessageResponse
from ..config.settings import settings
import logging
from ..utils.redis_client import RedisClient
from ..config.redis_config import REDIS_CONFIG

logger = logging.getLogger(__name__)

class FCMService:
    def __init__(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
            firebase_admin.initialize_app(cred)
        self.redis_client = RedisClient(**REDIS_CONFIG)
        self.token_cache_prefix = "fcm_token:"
        self.token_cache_expire = 86400  # 24小时过期
        self.topic_subscribers_prefix = "topic_subscribers:"
        self.topic_cache_expire = 3600  # 1小时过期
        self.rate_limit_prefix = "rate_limit:"
        self.rate_limit_window = 3600  # 1小时窗口
        self.max_messages_per_hour = 1000  # 每小时最大消息数

    async def send_message(
        self,
        message: FCMMessage,
        target: MessageTarget
    ) -> MessageResponse:
        """
        Send FCM message to specified target(s)
        """
        try:
            # 检查发送频率限制
            if not self._check_rate_limit(target):
                raise Exception("Rate limit exceeded")

            # Build the message
            fcm_message = messaging.Message(
                notification=messaging.Notification(
                    title=message.title,
                    body=message.body
                ),
                data=message.data or {},
                android=messaging.AndroidConfig(
                    priority="high" if message.priority == "high" else "normal",
                    ttl=message.ttl
                ),
                apns=messaging.APNSConfig(
                    headers={
                        "apns-priority": "10" if message.priority == "high" else "5"
                    }
                )
            )

            # Set the target
            if target.tokens:
                fcm_message.token = target.tokens[0]  # For single token
                if len(target.tokens) > 1:
                    # For multiple tokens, use multicast
                    response = messaging.send_multicast(
                        messaging.MulticastMessage(
                            tokens=target.tokens,
                            notification=fcm_message.notification,
                            data=fcm_message.data,
                            android=fcm_message.android,
                            apns=fcm_message.apns
                        )
                    )
                    return MessageResponse(
                        message_id=str(response.responses[0].message_id),
                        success=response.failure_count == 0,
                        error=None if response.failure_count == 0 else f"{response.failure_count} messages failed to send"
                    )
            elif target.topic:
                fcm_message.topic = target.topic
            elif target.condition:
                fcm_message.condition = target.condition

            # Send the message
            response = messaging.send(fcm_message)
            
            # 更新发送计数
            self._update_rate_limit(target)
            return MessageResponse(
                message_id=str(response),
                success=True,
                error=None
            )

        except Exception as e:
            logger.error(f"Error sending FCM message: {str(e)}")
            return MessageResponse(
                message_id="",
                success=False,
                error=str(e)
            )

    async def subscribe_to_topic(self, tokens: List[str], topic: str) -> bool:
        """
        Subscribe devices to a topic
        """
        try:
            success = await self._subscribe_to_topic_firebase(tokens, topic)
            if success:
                # 更新缓存
                cache_key = f"{self.topic_subscribers_prefix}{topic}"
                self.redis_client.delete(cache_key)  # 强制下次重新获取
            return success
        except Exception as e:
            logger.error(f"Error subscribing to topic: {str(e)}")
            return False

    async def unsubscribe_from_topic(self, tokens: List[str], topic: str) -> bool:
        """
        Unsubscribe devices from a topic
        """
        try:
            success = await self._unsubscribe_from_topic_firebase(tokens, topic)
            if success:
                # 更新缓存
                cache_key = f"{self.topic_subscribers_prefix}{topic}"
                self.redis_client.delete(cache_key)  # 强制下次重新获取
            return success
        except Exception as e:
            logger.error(f"Error unsubscribing from topic: {str(e)}")
            return False

    async def validate_token(self, token: str) -> bool:
        """
        Validate if an FCM token is still valid
        """
        try:
            # 先检查缓存
            cache_key = f"{self.token_cache_prefix}{token}"
            validation_result = self.redis_client.get(cache_key)
            
            if validation_result is not None:
                return validation_result

            # 缓存未命中，进行实际验证
            is_valid = await self._validate_token_with_firebase(token)
            
            # 存入缓存
            self.redis_client.set(cache_key, is_valid, self.token_cache_expire)
            return is_valid
        except Exception as e:
            logger.error(f"Error validating token: {str(e)}")
            return False

    def _check_rate_limit(self, target: Dict) -> bool:
        """
        检查速率限制
        """
        target_key = f"{target.get('type', 'unknown')}:{target.get('value', 'unknown')}"
        cache_key = f"{self.rate_limit_prefix}{target_key}"
        count = self.redis_client.get_counter(cache_key) or 0
        return count < self.max_messages_per_hour

    def _update_rate_limit(self, target: Dict):
        """
        更新速率限制计数
        """
        target_key = f"{target.get('type', 'unknown')}:{target.get('value', 'unknown')}"
        cache_key = f"{self.rate_limit_prefix}{target_key}"
        self.redis_client.increment_counter(cache_key)

    async def _send_fcm_message(self, message: Dict, target: Dict) -> Dict:
        """
        实际发送FCM消息的实现
        """
        # 实现发送FCM消息的逻辑
        return {"message_id": "sample_message_id"}

    async def _validate_token_with_firebase(self, token: str) -> bool:
        """
        使用Firebase验证token
        """
        # 实现token验证的逻辑
        return True

    async def _subscribe_to_topic_firebase(self, device_tokens: List[str], topic: str) -> bool:
        """
        使用Firebase订阅主题
        """
        # 实现订阅主题的逻辑
        return True

    async def _unsubscribe_from_topic_firebase(self, device_tokens: List[str], topic: str) -> bool:
        """
        使用Firebase取消订阅主题
        """
        # 实现取消订阅的逻辑
        return True 