import pymysql
from pymysql.constants import CLIENT
import os
from dotenv import load_dotenv
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

def create_connection():
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor
        #autocommit=True
    )
    return connection
def execute_query(query):
    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

def execute_query2(query):
    connection = create_connection()
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
    return True

def read_from_db(query):
    connection = create_connection()
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result

def insert_product(product_name,product_size,unit_price):
    query = f"""
        INSERT INTO products (product_name, product_size, unit_price)
        VALUES
        ('{product_name}','{product_size}',{unit_price})
        """
    execute_query2(query)
    print("New items successfully saved to database")
    return True
    
def get_unique_id(new_item_name,item_type: str = "order"):
    connection = create_connection()
    sql = f"""SELECT 
	    *
        FROM {item_type}s
        WHERE {item_type}_name = "{new_item_name}";"""
    with connection.cursor() as cursor:
        cursor.execute(sql)
        full_result = cursor.fetchall()
        id_type = f"{item_type}_id"
        new_item_id = full_result[0][id_type]
    return new_item_id

def insert_courier(new_item_name, new_item_number, servicing_area):
    query = f"""
        INSERT INTO couriers (courier_name, courier_phone_number, servicing_area)
        VALUES
        ('{new_item_name}','{new_item_number}','{servicing_area}')
        """
    execute_query2(query)
    print("New items successfully saved to database")
    return True