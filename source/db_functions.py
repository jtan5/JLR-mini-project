import pymysql
from pymysql.constants import CLIENT
import os
from dotenv import load_dotenv
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
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
####################################################################################################
###    INSERT_PRODUCT
####################################################################################################
def insert_product(product_name,product_size,unit_price):
    query = f"""
        INSERT INTO products (product_name, product_size, unit_price)
        VALUES
        ('{product_name}','{product_size}',{unit_price})
        """
    execute_query(query)
    print("New items successfully saved to database")
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
        INSERT INTO couriers (courier_name, courier_phone_number, servicing_area)
        VALUES
        ('{new_item_name}','{new_item_number}','{servicing_area}')
        """
    execute_query(query)
    print("New items successfully saved to database")
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
    print("New items successfully saved to database")
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
    return servicing_area_list[0]["servicing_area"]
####################################################################################################
####################################################################################################
###    UPDATE STOCK LEVEL AFTER ORDER
####################################################################################################
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