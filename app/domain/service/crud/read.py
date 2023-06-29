from typing import Optional

from domain.entity.user import User
import domain.repository.user as user_repository

def read(user_id: str) -> dict:
    user: Optional[User] = user_repository.get_user_by_id(user_id)
    
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