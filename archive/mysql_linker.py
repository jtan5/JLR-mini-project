import pymysql.cursors
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
# Connect to the database
connection = pymysql.connect(host='172.17.0.1',
                             user='myuser',
                             password='mypassword',
                             database='demo_db',
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        # Create a new record
        #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        sql = "select * from person;"
        #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        cursor.execute(sql)
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        #sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        sql = "select * from person;"
        #cursor.execute(sql, ('webmaster@python.org',))
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)