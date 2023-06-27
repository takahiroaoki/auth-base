from typing import Optional

from src.domain.entity.user import User
import src.schema.login as login_schema
import src.domain.repository.user as user_repository

async def login(login_info: login_schema.LoginInfo) -> login_schema.LoginResult:
    user: Optional[User] = await user_repository.get_user_by_email(login_info.email)
    if user and user.password == login_info.password:
        return login_schema.LoginResult(is_success = True)
    else:
        return login_schema.LoginResult(is_success = False)