import os

import mysql.connector

MYSQL_HOST=os.environ["MYSQL_HOST"]
MYSQL_DATABASE=os.environ["MYSQL_DATABASE"]
MYSQL_USER=os.environ["MYSQL_USER"]
MYSQL_PASSWORD=os.environ["MYSQL_PASSWORD"]
MYSQL_PORT=os.environ["MYSQL_PORT"]

def get_connection():
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        db=MYSQL_DATABASE,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD
    )
    return connection