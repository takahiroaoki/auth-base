from typing import Optional

from domain.entity.user import User
import schema.login as login_schema
import domain.repository.user as user_repository
import domain.util.hash as hash_util

def login(login_info: login_schema.LoginInfo) -> login_schema.LoginResult:
    user: Optional[User] = user_repository.get_user_by_email(login_info.email)
    
    if user and user.password == hash_util.get_hash_sha256(login_info.password):
        return login_schema.LoginResult(is_success = True)
    else:
        return login_schema.LoginResult(is_success = False)