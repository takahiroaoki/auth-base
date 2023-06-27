from typing import Optional
from src.domain.entity.user import User

async def get_user_by_email(user_email: str) -> Optional[User]:
    user: User = User()
    user.email = user_email
    user.password = "password"
    return user