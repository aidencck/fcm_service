from fastapi import HTTPException, status

class FCMException(HTTPException):
    """Base exception for FCM related errors"""
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=status_code, detail=detail) 