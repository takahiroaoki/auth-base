# change database
USE authbase;

# initialize tables
DROP TABLE IF EXISTS users;

# 'users' table
CREATE TABLE users (
    user_id INT(10) NOT NULL AUTO_INCREMENT,
    user_email VARCHAR(100) NOT NULL UNIQUE,
    user_password VARCHAR(100) NOT NULL,
    del_flg BOOLEAN DEFAULT 0,
    PRIMARY KEY(user_id)
);

INSERT INTO users (
    user_email,
    user_password
) VALUES (
    "user@example.com",
    "password"
);