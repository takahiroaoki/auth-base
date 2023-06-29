from typing import Optional, Tuple

from domain.entity.user import User
import domain.repository.sql.query as query

def get_user_by_email(user_email: str, conn) -> Optional[User]:
    sql_stmt: str = query.get("user/get_user_by_email.sql")
    sql_params = {
        "user_email": user_email,
    }
    with conn, conn.cursor() as cursor:
        cursor.execute(sql_stmt, sql_params)
        result: Optional[Tuple] = cursor.fetchone()
        if result:
            user = User().set_id(result[0]).set_email(result[1]).set_password(result[2])
            return user
        else:
            return None

def get_user_by_id(user_id: str, conn) -> Optional[User]:
    sql_stmt: str = query.get("user/get_user_by_id.sql")
    sql_params = {
        "user_id": user_id,
    }
    with conn, conn.cursor() as cursor:
        cursor.execute(sql_stmt, sql_params)
        result: Optional[Tuple] = cursor.fetchone()
        if result:
            user = User().set_id(result[0]).set_email(result[1]).set_password(result[2])
            return user
        else:
            return None

def insert_user(create_info: User, conn) -> Optional[User]:
    sql_stmt: str = query.get("user/insert_user.sql")
    sql_params = {
        "user_email": create_info.get_email(),
        "user_password": create_info.get_password()
    }
    with conn, conn.cursor() as cursor:
        try:
            cursor.execute(sql_stmt, sql_params)
            user: Optional[User] = get_user_by_email(create_info.get_email(), conn)
            if user:
                conn.commit()
                return user
            else:
                raise Exception()
        except:
            conn.rollback()
            return None