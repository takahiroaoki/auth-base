SELECT
    user_id,
    user_email,
    user_password
FROM
    users
WHERE
    user_email = %(user_email)s
    AND del_flg = 0