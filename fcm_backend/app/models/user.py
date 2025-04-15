from pydantic import BaseModel
from typing import Optional, Dict, List
from datetime import datetime
from enum import Enum

# A data model holding detailed device information
class DeviceInfo(BaseModel):
    device_id: str  # Unique identifier for the device
    device_model: Optional[str] = None  # Model or brand of the device
    device_os: Optional[str] = None  # Operating system name (e.g., Android, iOS)
    device_os_version: Optional[str] = None  # Version of the operating system
    app_version: Optional[str] = None  # Version of the application installed on the device
    push_token: Optional[str] = None  # Token used for push notifications
    phone_number: Optional[str] = None  # Phone number associated with the device (if any)
    imei: Optional[str] = None  # International Mobile Equipment Identity
    carrier: Optional[str] = None  # Mobile service carrier or provider

# A request model used for creating a new user
class CreateUserRequest(BaseModel):
    platform: str  # Platform type (web, android, ios)
    app_id: str  # Application identifier
    device_info: Optional[DeviceInfo] = None  # Optional device info for the new user

# A response model containing user-specific details
class UserResponse(BaseModel):
    uid: str  # Unique user ID
    platform: str  # User's platform
    app_id: str  # Application identifier for the user
    device_info: Optional[DeviceInfo] = None  # User's device information
    created_at: datetime  # Timestamp of user creation
    last_sign_in: Optional[datetime] = None  # Timestamp of the user's last sign-in

# A request model for updating a user's device information
class UpdateDeviceInfoRequest(BaseModel):
    device_info: DeviceInfo  # The new device information to be updated

# Enumeration of user subscription tiers
class SubscriptionTier(str, Enum):
    FREE = "free"
    BASIC = "basic"
    PREMIUM = "premium"

# Enumeration of possible subscription statuses
class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    TRIAL = "trial"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

# Enumeration of possible payment methods
class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"

# A data model for billing addresses, used in subscription or payment contexts
class BillingAddress(BaseModel):
    street: str  # Street address
    city: str  # City name
    state: str  # State or region
    country: str  # Country name
    postal_code: str  # Postal or ZIP code

# A history record of a user's subscription, including tier, status, and payment details
class SubscriptionHistory(BaseModel):
    tier: str  # The subscription tier during this history record
    status: SubscriptionStatus  # The subscription status at the time
    start_date: datetime  # Subscription start date
    end_date: Optional[datetime]  # Subscription end date, if applicable
    payment_method: Optional[PaymentMethod]  # The payment method used for this subscription
    billing_address: Optional[BillingAddress]  # The billing address used for this subscription record

# A data model representing a user, including subscription and billing details
class User(BaseModel):
    id: str  # Unique identifier for the user
    email: str  # The user's email
    subscription_tier: str = "free"  # Current subscription tier
    subscription_status: SubscriptionStatus = SubscriptionStatus.TRIAL  # Current subscription status
    subscription_start_date: datetime = datetime.now()  # Start date of the user's subscription
    subscription_end_date: Optional[datetime] = None  # End date of the user's subscription, if any
    payment_method: Optional[PaymentMethod] = None  # Payment method associated with this user
    billing_address: Optional[BillingAddress] = None  # Billing address associated with this user
    subscription_history: List[SubscriptionHistory] = []  # A record of the user's subscription changes
    api_key: Optional[str] = None  # API key used for authentication
    is_active: bool = True  # Whether the user is currently active

    class Config:
        from_attributes = True  # Enables model fields to map from object attributes