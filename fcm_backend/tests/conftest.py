import pytest
import os
from fastapi.testclient import TestClient
from app.config.settings import settings
from app.main import app
import firebase_admin
from firebase_admin import auth
import uuid

@pytest.fixture(scope="session")
def test_client():
    return TestClient(app)

@pytest.fixture(scope="session")
def firebase_app():
    # Use test credentials
    cred = firebase_admin.credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
    return firebase_admin.initialize_app(cred, name=str(uuid.uuid4()))

@pytest.fixture(scope="function")
def test_user(firebase_app):
    # Create a test user
    user = auth.create_user(
        email=f"test_{uuid.uuid4()}@example.com",
        password="testpassword123",
        display_name="Test User"
    )
    yield user
    # Clean up
    auth.delete_user(user.uid)

@pytest.fixture(scope="function")
def test_device_info():
    return {
        "device_id": "test_device_123",
        "device_model": "Test Device",
        "device_os": "Test OS",
        "device_os_version": "1.0.0",
        "app_version": "1.0.0",
        "push_token": "test_push_token_123"
    }
