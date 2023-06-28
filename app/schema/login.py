from typing import Optional
from pydantic import BaseModel, Field

"""
Request
"""
class LoginRequest(BaseModel):
    user_email: str
    user_password: str

"""
Response
"""
class UserData(BaseModel):
    user_id: str = Field("", description = "user_id")
    user_email: str = Field("", description = "user_email")

class Result(BaseModel):
    is_success: bool = Field(False, description = "Whether the login is success or not.")
    user_data: Optional[UserData] = Field(None, description = "user's data if the login is success")

class LoginResponse(BaseModel):
    result: Result = Field(Result(), description = "result of the request")


