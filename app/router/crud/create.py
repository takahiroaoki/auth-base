from fastapi import APIRouter

import schema.crud.create as create_schema
from domain.entity.user import User
import domain.service.crud.create as create_service

router = APIRouter()

@router.post("/create", response_model=create_schema.Response)
def create(request: create_schema.Request):
    create_info: User = User().set_email(request.user_email).set_password(request.user_password)
    create_result: dict = create_service.create(create_info)
    if create_result.get("is_success"):
        return create_schema.Response(
            contents = create_schema.Contents(
                is_success = create_result.get("is_success"),
                user_info = create_schema.UserInfo(
                    user_id = create_result.get("user_id"),
                    user_email = create_result.get("user_email")
                )
            )
        )
    else:
        return create_schema.Response(
            contents = create_schema.Contents(
                is_success = create_result.get("is_success")
            )
        )