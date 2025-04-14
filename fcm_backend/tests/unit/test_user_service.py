import pytest
from app.services.user_service import UserService
from app.models.user import DeviceInfo

@pytest.mark.asyncio
async def test_create_user(test_device_info):
    service = UserService()
    
    # Test creating a web user
    web_user_id = await service.create_user(
        platform="web",
        app_id="test_app",
        device_info=test_device_info
    )
    assert web_user_id is not None
    
    # Test creating an android user
    android_user_id = await service.create_user(
        platform="android",
        app_id="test_app",
        device_info=test_device_info
    )
    assert android_user_id is not None
    assert android_user_id != web_user_id
    
    # Test creating an ios user
    ios_user_id = await service.create_user(
        platform="ios",
        app_id="test_app",
        device_info=test_device_info
    )
    assert ios_user_id is not None
    assert ios_user_id != web_user_id
    assert ios_user_id != android_user_id

@pytest.mark.asyncio
async def test_get_user_info(test_device_info):
    service = UserService()
    
    # Create a test user
    user_id = await service.create_user(
        platform="web",
        app_id="test_app",
        device_info=test_device_info
    )
    
    # Get user info
    user_info = await service.get_user_info(user_id)
    
    # Verify user info
    assert user_info["uid"] == user_id
    assert user_info["platform"] == "web"
    assert user_info["app_id"] == "test_app"
    assert user_info["device_info"] == test_device_info

@pytest.mark.asyncio
async def test_update_user_device_info(test_device_info):
    service = UserService()
    
    # Create a test user
    user_id = await service.create_user(
        platform="web",
        app_id="test_app",
        device_info=test_device_info
    )
    
    # Update device info
    new_device_info = {
        "device_id": "new_device_123",
        "device_model": "New Device",
        "device_os": "New OS",
        "device_os_version": "2.0.0",
        "app_version": "2.0.0",
        "push_token": "new_push_token_123"
    }
    
    success = await service.update_user_device_info(user_id, new_device_info)
    assert success is True
    
    # Verify update
    user_info = await service.get_user_info(user_id)
    assert user_info["device_info"] == new_device_info
