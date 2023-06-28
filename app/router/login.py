from fastapi import APIRouter

import schema.login as login_schema
import domain.service.login as login_service
from domain.entity.user import User

router = APIRouter()

@router.post("/login", response_model=login_schema.LoginResponse)
def login(login_request: login_schema.LoginRequest):
    login_info = User().set_email(login_request.user_email).set_password(login_request.user_password)
    result: dict = login_service.login(login_info)
    
    if result.get("is_success"):
        return login_schema.LoginResponse(
            result = login_schema.Result(
                is_success = result.get("is_success"),
                user_data = login_schema.UserData(
                    user_id = result.get("user_id"),
                    user_email = result.get("user_email")
                )
            )
        )
    else:
        return login_schema.LoginResponse(
            result = login_schema.Result(
                is_success = result["is_success"]
            )
        )