# this module generally controls the opening and closing of files and the mappings

from logging import exception
import os
import json
import csv
from datetime import datetime
from pathlib import Path
import string
import pymysql
from pymysql.constants import CLIENT
import pymysql.cursors

from dotenv import load_dotenv
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Connect to the database
# connection = pymysql.connect(
#     host=host,
#     user=user,
#     password=password,
#     database=database,
#     client_flag=CLIENT.MULTI_STATEMENTS,
# )




####################################################################################################
###     INITIALISE DB
####################################################################################################

def initialize_db(sql_file_path):
    with open(sql_file_path, "r") as f:
        query = f.read()
        execute_on_db(query)


####################################################################################################
###     EXECUTE ON DB
####################################################################################################
def execute_on_db(query):
#Connect to the database
    connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    client_flag=CLIENT.MULTI_STATEMENTS,
)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    
####################################################################################################
####################################################################################################
###     IMPORT PRODUCT_DB
####################################################################################################
####################################################################################################

def import_product_db():   
    sql=("""
            SELECT
            product_name,
            unit_price,
            stock,
            product_id,
            product_size
            from products""")
    return read_from_db(sql)

####################################################################################################
####################################################################################################
###     IMPORT COURIER_DB
####################################################################################################
####################################################################################################

def import_courier_db():   
    sql=("""
            SELECT
            courier_id,
            courier_name,
            courier_phone_number,
            servicing_area,
            availability
            from couriers""")
    return read_from_db(sql)

####################################################################################################
####################################################################################################
###     IMPORT CUSTOMER_DB
####################################################################################################
####################################################################################################

def import_customer_db():   
    sql=("""
            SELECT
            customer_name,
            customer_address,
            customer_postcode,
            servicing_area,
            customer_id
            from customers""")
    return read_from_db(sql)

####################################################################################################
####################################################################################################
###     IMPORT ORDER_DB
####################################################################################################
####################################################################################################

def import_order_db():   
    sql=("""
            SELECT
            *
            from orders""")
    return read_from_db(sql)

####################################################################################################
###    CREATE_CONNECTION
####################################################################################################
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
####################################################################################################
###    EXECUTE_QUERY
####################################################################################################
def execute_query(query):
    try:
        connection = create_connection()
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
        return True
    except Exception as e:
        if e[0] == 1451:
            print("There is a dependency associated with this element; please check there are no open orders associated with this element.")
        else:
            print(e)

def read_from_db(query):
    connection = create_connection()
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
    return result
####################################################################################################
###    INSERT_PRODUCT
####################################################################################################
def insert_product(product_name,stock,unit_price,product_size):
    query = f"""
        INSERT INTO products (product_name, stock, unit_price, product_size)
        VALUES
        ('{product_name}',{stock},{unit_price},'{product_size}')
        """
    execute_query(query)
    #print("New items successfully saved to database")
    return True
####################################################################################################
###    GET_UNIQUE_ID
####################################################################################################
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
####################################################################################################
###    INSERT_COURIER
####################################################################################################
def insert_courier(new_item_name, new_item_number, servicing_area):
    query = f"""
        INSERT INTO couriers (courier_name, courier_phone_number, servicing_area,availability)
        VALUES
        ('{new_item_name}','{new_item_number}','{servicing_area}',1)
        """
    execute_query(query)
    #print("New items successfully saved to database")
    return True
####################################################################################################
###    INSERT_CUSTOMER
####################################################################################################
def insert_customer(name, address, postcode, servicing_area):
    query = f"""
        INSERT INTO customers (customer_name, customer_address, customer_postcode, servicing_area)
        VALUES
        ('{name}','{address}','{postcode}','{servicing_area}')
        """
    execute_query(query)
    #print("New items successfully saved to database")
    return True
####################################################################################################
###    GET_NEW_CUSTOMER_ID
####################################################################################################
def get_new_customer_id(name, address):
    query = f"""
        SELECT 
        customer_id
        FROM customers
        WHERE CONCAT_WS("_",customer_name,customer_address) = '{name}_{address}'
        """
    output = read_from_db(query) #output: [{'customer_id': 9}]
    return output[0]['customer_id'] #gives an integer output
####################################################################################################
###    INSERT_ORDER
####################################################################################################
def insert_order(order_dict: dict):
    query = f"""
        INSERT INTO orders (courier_id, customer_id, order_status, temp_description)
        VALUES
        ({order_dict['courier_id']},{order_dict['customer_id']},'{order_dict['order_status']}',{order_dict['temp_description']})
        """
    execute_query(query)
    
    query = f"""
        SELECT 
        order_id
        FROM orders
        WHERE temp_description = {order_dict['temp_description']}
        """
    order_id = read_from_db(query)
    #print("New items successfully saved to database")
    return order_id[0]["order_id"]
####################################################################################################
###    GET_MATCHING_COURIER
####################################################################################################
def get_matching_courier(servicing_area: str):
    query = f"""
        SELECT 
    *
    FROM couriers
    WHERE servicing_area = "{servicing_area}" AND availability = 1;"""
    return read_from_db(query)
####################################################################################################
###    INSERT_ORDER_PRODUCTS
####################################################################################################
def insert_order_products(order_products_list:list):
    #create new query based on len of list
    query = """
            INSERT INTO order_prod(order_id, customer_id, courier_id, product_id, product_quantity)
            VALUES"""
    for i, _ in enumerate(order_products_list):
        statement_to_add = f"({order_products_list[i]['order_id']},{order_products_list[i]['customer_id']},{order_products_list[i]['courier_id']},{order_products_list[i]['product_id']},{order_products_list[i]['product_quantity']})"
        if i < len(order_products_list) -1: # we don't want to add the comma in the last entry
            query = f"{query}{statement_to_add},"
        else: # for the last entry no comma
            query = f"{query}{statement_to_add}"
    # query to mimic = f """
    #         INSERT INTO order_prod(order_id, courier_id, product_id, product_quantity)
    #         VALUES(1,3,4,1),
	# 	    (1,2,2,1)"""
    # print(query)
    # input("WAIT")
    execute_query(query)
    return True
    
    
def get_customer_servicing_area(customer_id):
    query = f"""
            select
            *
            from customers
            WHERE customer_id = {customer_id}
            """
    servicing_area_list = read_from_db(query)
    customer_servicing_area = servicing_area_list[0]['servicing_area']
    return customer_servicing_area

####################################################################################################
###    UPDATE STOCK LEVEL AFTER ORDER
####################################################################################################

#UPDATE `cafe_db`.`products` SET `stock` = '47' WHERE (`product_id` = '3');
#update products set stock = stock-{order_products_list[i]['product_quantity']} where product_id = {order_products_list[i]['product_id']};
def update_stock(order_products_list: list):
    #create new query based on len of list
    for i, _ in enumerate(order_products_list):
        query = f"""update products set stock = stock-{order_products_list[i]['product_quantity']} where product_id = {order_products_list[i]['product_id']};"""
        execute_query(query)
    return True

####################################################################################################
####################################################################################################
###    RETURN INVOICE VIEW
####################################################################################################
####################################################################################################
def return_invoice_list(order_id:int):
    query = f"""
            select 
            op.order_id,
            o.order_status,
            cu.customer_name,
            c.courier_name,
            p.product_name,
            op.product_quantity as quantity,
            p.unit_price * op.product_quantity as subtotal,
            round(p.unit_price * op.product_quantity * 0.2,2) as itemVAT,
            round(p.unit_price * op.product_quantity * 1.2,2) as total_inc_VAT
            FROM order_prod op
            LEFT JOIN customers cu ON (op.customer_id = cu.customer_id)
            LEFT JOIN orders o ON (op.order_id = o.order_id)
            LEFT JOIN products p ON (op.product_id = p.product_id)
            LEFT JOIN couriers c ON (op.courier_id = c.courier_id)
            where op.order_id = {order_id}
            """
    return read_from_db(query)

####################################################################################################
def return_invoice_total(order_id:int):
    query = f"""
            select 
            op.order_id,
            o.order_status,
            round(sum(p.unit_price * op.product_quantity * 1.2),2) as total_amount_due
            FROM order_prod op
            LEFT JOIN customers cu ON (op.customer_id = cu.customer_id)
            LEFT JOIN orders o ON (op.order_id = o.order_id)
            LEFT JOIN products p ON (op.product_id = p.product_id)
            LEFT JOIN couriers c ON (op.courier_id = c.courier_id)
            where op.order_id = {order_id}
            """
    output = read_from_db(query)
    return output[0]['total_amount_due']

####################################################################################################
###    RETURN ORDER STATUS
####################################################################################################
def return_order_status(order_status: str):
    query = f"""
            select 
            distinct(op.order_id),
            o.order_status,
            cu.customer_name,
            c.courier_name
            FROM order_prod op
            LEFT JOIN customers cu ON (op.customer_id = cu.customer_id)
            LEFT JOIN orders o ON (op.order_id = o.order_id)
            LEFT JOIN products p ON (op.product_id = p.product_id)
            LEFT JOIN couriers c ON (op.courier_id = c.courier_id)
            where o.order_status = '{order_status}';"""
    return read_from_db(query)
####################################################################################################
###    RETURN ORDER STATUS ALL
####################################################################################################
def return_order_status_all():
    query = f"""
            select 
            distinct(op.order_id),
            o.order_status,
            cu.customer_name,
            c.courier_name
            FROM order_prod op
            LEFT JOIN customers cu ON (op.customer_id = cu.customer_id)
            LEFT JOIN orders o ON (op.order_id = o.order_id)
            LEFT JOIN products p ON (op.product_id = p.product_id)
            LEFT JOIN couriers c ON (op.courier_id = c.courier_id)
            """
    return read_from_db(query)
####################################################################################################
###    UPDATE ORDER STATUS
####################################################################################################
def update_status(order_id:int, status:str):
    query = f"""
            UPDATE orders SET order_status = "{status}" WHERE(order_id = {order_id});"""
    execute_query(query)
    return True
####################################################################################################
###    UPDATE ITEM STATUS
####################################################################################################
def change_item(update_list:list, category:str):
    for i, _ in enumerate(update_list):
        query_body = ""
        query_header = f"""UPDATE {category}s SET """

        ki = 0
        for k,v in update_list[i].items():
            if ki < len(update_list[i])- 2: #removing a k:v pair for the item_id
                comma_status = ","
            else:
                comma_status = ""
            if k != f"{category}_id":
                if isinstance(v, str):
                    query_body = f"{query_body} {k}='{v}'{comma_status}"
                else:
                    query_body = f"{query_body} {k}={v}{comma_status}"
            else: # when its item_id
                query_footer = f"WHERE {category}_id IN ({v})"
            ki += 1
        #assembly query here
        final_query = f'{query_header} {query_body} {query_footer}'
        print(final_query)
        execute_query(final_query)
        #run upload here

    #query to mimic =f """UPDATE products
	#                       SET 
	# 	                        product_size = "S",
    #                           unit_price = 1.02,
    #                           stock = 49,
    #                           product_name = "Chips"
	# 	                    WHERE product_id IN (3);"
 
 
 
 
####################################################################################################
###    DELETING CUSTOMER 
####################################################################################################
def test_query():
    try:
        query = "DELETE FROM `cafe_db`.`customers` WHERE (`customer_id` = '10');"
        execute_query(query)
        return True
    except Exception as e:
        print (e)
        