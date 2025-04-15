from pydantic import BaseModel
from typing import Optional, Dict, List
from datetime import datetime
from enum import Enum

class DeviceInfo(BaseModel):
    device_id: str
    device_model: Optional[str] = None
    device_os: Optional[str] = None
    device_os_version: Optional[str] = None
    app_version: Optional[str] = None
    push_token: Optional[str] = None
    phone_number: Optional[str] = None
    imei: Optional[str] = None
    carrier: Optional[str] = None

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

class SubscriptionTier(str, Enum):
    FREE = "free"
    BASIC = "basic"
    PREMIUM = "premium"

class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    TRIAL = "trial"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"

class BillingAddress(BaseModel):
    street: str
    city: str
    state: str
    country: str
    postal_code: str

class SubscriptionHistory(BaseModel):
    tier: str
    status: SubscriptionStatus
    start_date: datetime
    end_date: Optional[datetime]
    payment_method: Optional[PaymentMethod]
    billing_address: Optional[BillingAddress]

class User(BaseModel):
    id: str
    email: str
    subscription_tier: str = "free"
    subscription_status: SubscriptionStatus = SubscriptionStatus.TRIAL
    subscription_start_date: datetime = datetime.now()
    subscription_end_date: Optional[datetime] = None
    payment_method: Optional[PaymentMethod] = None
    billing_address: Optional[BillingAddress] = None
    subscription_history: List[SubscriptionHistory] = []
    api_key: Optional[str] = None
    is_active: bool = True
    
    class Config:
        from_attributes = True 