from fastapi import APIRouter, Depends, HTTPException
from app.services.fcm_service import FCMService
from app.core.security import get_current_user
from app.models.user import User
from typing import Optional, List

router = APIRouter(prefix="/fcm", tags=["fcm"])

@router.post("/send")
async def send_message(
    token: str,
    title: str,
    body: str,
    data: Optional[dict] = None,
    current_user: User = Depends(get_current_user)
):
    """
    Send a message to a specific device using FCM.
    """
    try:
        message_id = FCMService.send_message(token, title, body, data)
        return {"message_id": message_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/send-multicast")
async def send_multicast(
    tokens: List[str],
    title: str,
    body: str,
    data: Optional[dict] = None,
    current_user: User = Depends(get_current_user)
):
    """
    Send a message to multiple devices using FCM.
    """
    try:
        response = FCMService.send_multicast(tokens, title, body, data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 