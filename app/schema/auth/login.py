from typing import Optional
from pydantic import BaseModel, Field

"""
Request
"""
class Request(BaseModel):
    user_email: str
    user_password: str

"""
Response
"""
class UserInfo(BaseModel):
    user_id: str = Field("", description = "user_id")
    user_email: str = Field("", description = "user_email")

class Contents(BaseModel):
    is_success: bool = Field(False, description = "Whether the login is success or not.")
    user_info: Optional[UserInfo] = Field(None, description = "user's information if the login is success")

class Response(BaseModel):
    contents: Contents = Field(Contents(), description = "Contents of the request")


