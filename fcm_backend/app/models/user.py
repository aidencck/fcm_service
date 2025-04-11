from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class DeviceInfo(BaseModel):
    device_id: str
    device_model: Optional[str] = None
    device_os: Optional[str] = None
    device_os_version: Optional[str] = None
    app_version: Optional[str] = None
    push_token: Optional[str] = None

class CreateUserRequest(BaseModel):
    platform: str  # web, android, ios
    app_id: str
    device_info: Optional[DeviceInfo] = None

class UserResponse(BaseModel):
    uid: str
    platform: str
    app_id: str
    device_info: Optional[DeviceInfo] = None
    created_at: datetime
    last_sign_in: Optional[datetime] = None

class UpdateDeviceInfoRequest(BaseModel):
    device_info: DeviceInfo 