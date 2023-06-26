from fastapi import APIRouter
import src.schema.login as login_schema

router = APIRouter()

@router.post("/login", response_model=login_schema.LoginResult)
async def login(login_info: login_schema.LoginInfo):
    if login_info.email == "user@example.com" and login_info.password == "password":
        return login_schema.LoginResult(is_success = True)
    else:
        return login_schema.LoginResult(is_success = False)