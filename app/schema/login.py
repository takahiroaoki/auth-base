from pydantic import BaseModel, Field

class LoginInfo(BaseModel):
    email: str
    password: str

class LoginResult(BaseModel):
    is_success: bool = Field(False, description = "Whether the login is success or not.")