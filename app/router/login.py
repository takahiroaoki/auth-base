from fastapi import APIRouter

import schema.login as login_schema
import domain.service.login as login_service

router = APIRouter()

@router.post("/login", response_model=login_schema.LoginResult)
def login(login_info: login_schema.LoginInfo):
    return login_service.login(login_info)