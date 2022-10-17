from db_functions import execute_query, execute_query2, insert_product

# import pymysql
# from pymysql.constants import CLIENT
# import os
# from dotenv import load_dotenv
# load_dotenv()
# host = os.environ.get("mysql_host")
# user = os.environ.get("mysql_user")
# password = os.environ.get("mysql_pass")
# database = os.environ.get("mysql_db")

my_query = """
            SELECT * FROM products
        """
# result = execute_query(my_query)
# for row in result:
#     print("product price:", float(row['price']),)

my_insert_query = """
    INSERT INTO products (`name`,`size`,`price`)
    VALUES
        ("Watermelon","S",33.99);
    """
    
# execute_query2(my_insert_query)

product_name = "Suwhi"
product_price = 10.33

insert_product(product_name, product_price)