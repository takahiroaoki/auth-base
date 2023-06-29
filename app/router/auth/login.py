from fastapi import APIRouter, Depends

import schema.auth.login as login_schema
import domain.service.auth.login as login_service
from domain.entity.user import User
import infrastructure.database as db

router = APIRouter()

@router.post("/login", response_model=login_schema.Response)
def login(request: login_schema.Request, conn = Depends(db.get_connection)):
    login_info = User().set_email(request.user_email).set_password(request.user_password)
    login_result: dict = login_service.login(login_info, conn)
    
    if login_result.get("is_success"):
        return login_schema.Response(
            contents = login_schema.Contents(
                is_success = login_result.get("is_success"),
                user_info = login_schema.UserInfo(
                    user_id = login_result.get("user_id"),
                    user_email = login_result.get("user_email")
                )
            )
        )
    else:
        return login_schema.Response(
            contents = login_schema.Contents(
                is_success = login_result.get("is_success")
            )
        )