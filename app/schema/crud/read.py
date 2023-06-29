from typing import Optional
from pydantic import BaseModel, Field

"""
Response
"""
class UserInfo(BaseModel):
    user_id: str = Field("", description = "user id")
    user_email: str = Field("", description = "user email")

class Contents(BaseModel):
    is_success: bool = Field(False, description = "Whether the operation is success or not.")
    user_info: Optional[UserInfo] = Field(None, description = "user's information if the operation is success")

class Response(BaseModel):
    contents: Contents = Field(Contents(), description = "Contents of the response")