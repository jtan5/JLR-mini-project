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
connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
with connection:
    with connection.cursor() as cursor:
        # Read a single record
        #sql = "SELECT * from person"
        sql = """SELECT *
                FROM person
                ORDER BY first_name desc"""
        cursor.execute(sql)
        result = cursor.fetchone() #use fetchall() to get a dictionary or fetchmany()
        print(result)