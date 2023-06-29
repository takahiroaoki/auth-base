SELECT
    user_id,
    user_email,
    user_password
FROM
    users
WHERE
    user_id = %(user_id)s
    AND del_flg = 0