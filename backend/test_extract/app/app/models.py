from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List


class FeedbackInput(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    rating: int = Field(..., ge=1, le=5)
    message: str = Field(..., min_length=5, max_length=2000)
    tag: Optional[str] = "general"
    recaptcha_token: Optional[str] = None


class FeedbackItem(BaseModel):
    feedback_id: str
    created_at: str
    name: Optional[str]
    email: Optional[EmailStr]
    rating: int
    message: str
    tag: Optional[str]
