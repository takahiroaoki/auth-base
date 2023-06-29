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
            user = User().set_id(result[0]).set_email(result[1]).set_password(result[2])
            return user
        else:
            return None

def get_user_by_id(user_id: str) -> Optional[User]:
    sql_stmt: str = dbutil.get_query("user/get_user_by_id.sql")
    sql_params = {
        "user_id": user_id,
    }
    with dbutil.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql_stmt, sql_params)
        result: Optional[Tuple] = cursor.fetchone()
        if result:
            user = User().set_id(result[0]).set_email(result[1]).set_password(result[2])
            return user
        else:
            return None