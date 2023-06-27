from typing import Optional, Tuple
from domain.entity.user import User
import domain.repository.database.dbutil as dbutil

async def get_user_by_email(user_email: str) -> Optional[User]:
    sql: str = (await dbutil.get_query("user/get_user_by_email.sql")).format(user_email = user_email)
    with await dbutil.get_connection() as conn:
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