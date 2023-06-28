from typing import Optional, Tuple
from domain.entity.user import User
import domain.repository.database.dbutil as dbutil

def get_user_by_email(user_email: str) -> Optional[User]:
    sql_stmt: str = dbutil.get_query("user/get_user_by_email.sql")
    sql_params = {
        "user_email": user_email,
    }
    with dbutil.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql_stmt, sql_params)
        result: Optional[Tuple] = cursor.fetchone()
        if result:
            user = User()
            user.id = result[0]
            user.email = result[1]
            user.password = result[2]
            return user
        else:
            return None