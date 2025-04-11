import firebase_admin
from firebase_admin import credentials, messaging
from typing import List, Optional, Dict, Any
from datetime import datetime
from ..models.fcm import FCMToken, FCMMessage, MessageTarget, MessageResponse
from ..config.settings import settings
import logging

logger = logging.getLogger(__name__)

class FCMService:
    def __init__(self):
        if not firebase_admin._apps:
            cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
            firebase_admin.initialize_app(cred)

    async def send_message(
        self,
        message: FCMMessage,
        target: MessageTarget
    ) -> MessageResponse:
        """
        Send FCM message to specified target(s)
        """
        try:
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
            response = messaging.subscribe_to_topic(tokens, topic)
            return response.success_count > 0
        except Exception as e:
            logger.error(f"Error subscribing to topic: {str(e)}")
            return False

    async def unsubscribe_from_topic(self, tokens: List[str], topic: str) -> bool:
        """
        Unsubscribe devices from a topic
        """
        try:
            response = messaging.unsubscribe_from_topic(tokens, topic)
            return response.success_count > 0
        except Exception as e:
            logger.error(f"Error unsubscribing from topic: {str(e)}")
            return False

    async def validate_token(self, token: str) -> bool:
        """
        Validate if an FCM token is still valid
        """
        try:
            # Try to send a test message
            message = messaging.Message(
                token=token,
                data={"type": "validation"}
            )
            messaging.send(message)
            return True
        except messaging.UnregisteredError:
            return False
        except Exception as e:
            logger.error(f"Error validating token: {str(e)}")
            return False 