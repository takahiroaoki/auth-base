from typing import Optional, Tuple
from src.domain.entity.user import User
import src.domain.repository.database as db

async def get_user_by_email(user_email: str) -> Optional[User]:
    sql: str = (await db.get_query("user/get_user_by_email.sql")).format(user_email = user_email)
    with await db.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        result: Optional[Tuple] = cursor.fetchone()
        if result:
            user: User = User()
            user.id = result[0]
            user.email = result[1]
            user.password = result[2]
            return user
        else:
            return None