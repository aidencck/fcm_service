import pytest
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

def test_create_user():
    # Test creating a web user
    response = client.post(
        "/api/v1/users/create",
        json={
            "platform": "web",
            "app_id": "test_app",
            "device_info": {
                "device_id": "web_browser_123",
                "device_model": "Chrome",
                "device_os": "Windows",
                "device_os_version": "10",
                "app_version": "1.0.0"
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "uid" in data
    assert data["platform"] == "web"
    assert data["app_id"] == "test_app"
    
    # Test creating an android user
    response = client.post(
        "/api/v1/users/create",
        json={
            "platform": "android",
            "app_id": "test_app",
            "device_info": {
                "device_id": "android_device_123",
                "device_model": "Pixel 6",
                "device_os": "Android",
                "device_os_version": "12",
                "app_version": "1.0.0",
                "push_token": "fcm_token_123"
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "uid" in data
    assert data["platform"] == "android"
    
    # Test creating an ios user
    response = client.post(
        "/api/v1/users/create",
        json={
            "platform": "ios",
            "app_id": "test_app",
            "device_info": {
                "device_id": "ios_device_123",
                "device_model": "iPhone 13",
                "device_os": "iOS",
                "device_os_version": "15.0",
                "app_version": "1.0.0",
                "push_token": "fcm_token_123"
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "uid" in data
    assert data["platform"] == "ios"

def test_get_user():
    # First create a user
    create_response = client.post(
        "/api/v1/users/create",
        json={
            "platform": "web",
            "app_id": "test_app",
            "device_info": {
                "device_id": "test_device_123",
                "device_model": "Test Device",
                "device_os": "Test OS",
                "device_os_version": "1.0.0",
                "app_version": "1.0.0"
            }
        }
    )
    assert create_response.status_code == 200
    user_id = create_response.json()["uid"]
    
    # Then get the user
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["uid"] == user_id
    assert data["platform"] == "web"
    assert data["app_id"] == "test_app"

def test_update_device_info():
    # First create a user
    create_response = client.post(
        "/api/v1/users/create",
        json={
            "platform": "web",
            "app_id": "test_app",
            "device_info": {
                "device_id": "test_device_123",
                "device_model": "Test Device",
                "device_os": "Test OS",
                "device_os_version": "1.0.0",
                "app_version": "1.0.0"
            }
        }
    )
    assert create_response.status_code == 200
    user_id = create_response.json()["uid"]
    
    # Then update device info
    response = client.put(
        f"/api/v1/users/{user_id}/device-info",
        json={
            "device_info": {
                "device_id": "new_device_123",
                "device_model": "New Device",
                "device_os": "New OS",
                "device_os_version": "2.0.0",
                "app_version": "2.0.0",
                "push_token": "new_push_token_123"
            }
        }
    )
    assert response.status_code == 200
    assert response.json() is True
    
    # Verify the update
    get_response = client.get(f"/api/v1/users/{user_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["device_info"]["device_id"] == "new_device_123"
    assert data["device_info"]["device_model"] == "New Device"
