from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class FCMToken(BaseModel):
    user_id: str
    device_token: str
    platform: str  # android, ios, web
    app_id: str
    created_at: datetime
    last_updated: datetime
    is_active: bool = True

class TopicSubscription(BaseModel):
    user_id: str
    topic: str
    app_id: str
    subscribed_at: datetime

class FCMMessage(BaseModel):
    title: Optional[str] = None
    body: str
    data: Optional[Dict[str, Any]] = None
    message_type: str  # system, promotion, alert, etc.
    priority: str = "normal"  # normal, high
    ttl: Optional[int] = None  # Time to live in seconds

class MessageTarget(BaseModel):
    tokens: Optional[List[str]] = None
    topic: Optional[str] = None
    condition: Optional[str] = None

class MessageResponse(BaseModel):
    message_id: str
    success: bool
    error: Optional[str] = None 