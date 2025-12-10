from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class FeedbackInput(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    message: str = Field(..., min_length=5, max_length=2000)
    recaptcha_token: Optional[str] = None
