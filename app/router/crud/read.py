from fastapi import APIRouter, Depends

import schema.crud.read as read_schema
import domain.service.crud.read as read_service
import infrastructure.database as db

router = APIRouter()

@router.get("/read", response_model=read_schema.Response)
def read(user_id: str, conn = Depends(db.get_connection)):
    read_result: dict = read_service.read(user_id, conn)
    if read_result.get("is_success"):
        return read_schema.Response(
            contents = read_schema.Contents(
                is_success = read_result.get("is_success"),
                user_info = read_schema.UserInfo(
                    user_id = read_result.get("user_id"),
                    user_email = read_result.get("user_email")
                )
            )
        )
    else:
        return read_schema.Response(
            contents = read_schema.Contents(
                is_success = read_result.get("is_success")
            )
        )