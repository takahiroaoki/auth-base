from typing import Optional, Tuple

from domain.entity.user import User
from domain.repository.database import dbutil

def get_user_by_email(user_email: str) -> Optional[User]:
    sql_stmt: str = dbutil.get_query("user/get_user_by_email.sql")
    sql_params = {
        "user_email": user_email,
    }
    with dbutil.get_connection() as conn, conn.cursor() as cursor:
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
    with dbutil.get_connection() as conn, conn.cursor() as cursor:
        cursor.execute(sql_stmt, sql_params)
        result: Optional[Tuple] = cursor.fetchone()
        if result:
            user = User().set_id(result[0]).set_email(result[1]).set_password(result[2])
            return user
        else:
            return None

def insert_user(create_info: User) -> Optional[User]:
    sql_stmt: str = dbutil.get_query("user/insert_user.sql")
    sql_params = {
        "user_email": create_info.get_email(),
        "user_password": create_info.get_password()
    }
    with dbutil.get_connection() as conn, conn.cursor(buffered = True) as cursor:
        try:
            cursor.execute(sql_stmt, sql_params)
            cursor.execute(dbutil.get_query("user/last_insert_id.sql"))
            user: User = User().set_id(cursor.fetchone()[0]).set_email(create_info.get_email())
            conn.commit()
            return user
        except Exception as e:
            print(e)
            conn.rollback()
            return None