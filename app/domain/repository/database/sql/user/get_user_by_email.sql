SELECT
    user_id,
    user_email,
    user_password
FROM
    users
WHERE
    user_email = '{user_email}'
    AND del_flg = 0