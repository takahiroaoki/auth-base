from fastapi import APIRouter

import src.schema.login as login_schema
import src.domain.service.login as login_service

router = APIRouter()

@router.post("/login", response_model=login_schema.LoginResult)
async def login(login_info: login_schema.LoginInfo):
    return await login_service.login(login_info)