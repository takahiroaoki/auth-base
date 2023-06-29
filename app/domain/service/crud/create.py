from typing import Optional

from domain.entity.user import User
import domain.repository.user as user_repository
import domain.util.hash as hash_util

def create(create_info: User) -> dict:
    user: Optional[User] = user_repository.insert_user(
        create_info.set_password(
            hash_util.get_hash_sha256(create_info.get_password())
        )
    )

    if user:
        return {
            "is_success": True,
            "user_id": user.get_id(),
            "user_email": user.get_email()
        }
    else:
        return {
            "is_success": False
        }