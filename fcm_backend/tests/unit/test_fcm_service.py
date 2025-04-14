import pytest
from app.services.fcm_service import FCMService
from app.models.fcm import FCMMessage, MessageTarget

@pytest.mark.asyncio
async def test_send_message():
    service = FCMService()
    
    # Test message
    message = FCMMessage(
        title="Test Title",
        body="Test Body",
        message_type="test",
        priority="normal"
    )
    
    # Test target
    target = MessageTarget(
        tokens=["test_token_123"]
    )
    
    # Send message
    response = await service.send_message(message, target)
    
    # Verify response
    assert response.message_id is not None
    assert response.success is True
    assert response.error is None

@pytest.mark.asyncio
async def test_subscribe_to_topic():
    service = FCMService()
    
    # Test subscription
    success = await service.subscribe_to_topic(
        tokens=["test_token_123"],
        topic="test_topic"
    )
    
    assert success is True

@pytest.mark.asyncio
async def test_unsubscribe_from_topic():
    service = FCMService()
    
    # Test unsubscription
    success = await service.unsubscribe_from_topic(
        tokens=["test_token_123"],
        topic="test_topic"
    )
    
    assert success is True

@pytest.mark.asyncio
async def test_validate_token():
    service = FCMService()
    
    # Test valid token
    is_valid = await service.validate_token("test_token_123")
    assert isinstance(is_valid, bool)
