from typing import Optional

from domain.entity.user import User
import domain.repository.user as user_repository
import domain.util.hash as hash_util

def login(login_info: User, conn) -> dict:
    user: Optional[User] = user_repository.get_user_by_email(login_info.get_email(), conn)
    
    if user and user.get_password() == hash_util.get_hash_sha256(login_info.get_password()):
        return {
            "is_success": True,
            "user_id": user.get_id(),
            "user_email": user.get_email()
        }
    else:
        return {
            "is_success": False
        }