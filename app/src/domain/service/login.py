import src.schema.login as login_schema

async def login(login_info: login_schema.LoginInfo) -> login_schema.LoginResult:
    if login_info.email == "sample@example.com" and login_info.password == "password":
        return login_schema.LoginResult(is_success = True)
    else:
        return login_schema.LoginResult(is_success = False)