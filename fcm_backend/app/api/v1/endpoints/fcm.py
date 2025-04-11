from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ...models.fcm import FCMToken, FCMMessage, MessageTarget, MessageResponse, TopicSubscription
from ...services.fcm_service import FCMService
from datetime import datetime

router = APIRouter()
fcm_service = FCMService()

@router.post("/send", response_model=MessageResponse)
async def send_message(
    message: FCMMessage,
    target: MessageTarget
):
    """
    Send FCM message to specified target(s)
    """
    return await fcm_service.send_message(message, target)

@router.post("/tokens/register", response_model=bool)
async def register_token(token: FCMToken):
    """
    Register a new FCM token for a user
    """
    # Here you would typically save the token to your database
    # For now, we'll just validate it
    return await fcm_service.validate_token(token.device_token)

@router.post("/topics/subscribe", response_model=bool)
async def subscribe_topic(subscription: TopicSubscription):
    """
    Subscribe a user's device to a topic
    """
    return await fcm_service.subscribe_to_topic(
        [subscription.device_token],
        f"{subscription.app_id}_{subscription.topic}"
    )

@router.post("/topics/unsubscribe", response_model=bool)
async def unsubscribe_topic(subscription: TopicSubscription):
    """
    Unsubscribe a user's device from a topic
    """
    return await fcm_service.unsubscribe_from_topic(
        [subscription.device_token],
        f"{subscription.app_id}_{subscription.topic}"
    )

@router.post("/tokens/validate", response_model=bool)
async def validate_token(token: str):
    """
    Validate if an FCM token is still valid
    """
    return await fcm_service.validate_token(token) 