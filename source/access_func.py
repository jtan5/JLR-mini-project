# this module generally controls the opening and closing of files and the mappings

import os
import json
import csv
from datetime import datetime
from pathlib import Path

from source.db_functions import read_from_db

# initialising global variables
dummy_dict = {"DEBUG DICT", "T1000", "Distructomatic T47"}


####################################################################################################
####################################################################################################
###     IMPORT PRODUCT_CSV
####################################################################################################
####################################################################################################

def import_product_csv():
    # sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    print("Current Directory: ", current_path)
    print("Parent Directory: ", parent_path)
    #products_file = os.path.join(current_path, "products", "cold_food.csv")
    products_path = os.path.join(current_path, "products")
    
    choice_list = []
    
    global food_dict
    food_dict = dict()
    
    for index, filename in enumerate(os.listdir(products_path)):
        print("printing filename", index, filename)
        # starting with an empty list, populating choicelist based on filenames, stripping out .csv
        clean_name = os.path.splitext(filename)[0]
        print(clean_name)
        choice_list.append(clean_name)
        globals()[os.path.splitext(filename)[0]] = []

        (os.path.join(products_path, filename))
        with open(os.path.join(products_path, filename), 'r') as file:
            reader_dict = csv.DictReader(file, delimiter=',')
            for index, row in enumerate(reader_dict):
                globals()[clean_name].append(row)
                header = row.keys
            #print(f"Final filename contents of file: {clean_name}: {globals()[clean_name]}")
            food_dict[clean_name] = globals()[clean_name]
    return food_dict

####################################################################################################
####################################################################################################
###     IMPORT PRODUCT_DB
####################################################################################################
####################################################################################################

def import_product_db():   
    sql=("""
            SELECT
            product_id,
            product_size,
            unit_price,
            product_name
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
            servicing_area
            from couriers""")
    return read_from_db(sql)
####################################################################################################
####################################################################################################
###     EXPORT PRODUCT_CSV
####################################################################################################
####################################################################################################
def export_product_csv(func_dict=[{"Dummy Order List": "I don't know"}]):
    # sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    products_path = os.path.join(current_path, "products")

    # getting the latest choice_list from food_dict
    choice_list = list(func_dict.keys())

    for key in func_dict.keys():
        globals()[key]
        filename = key + ".csv"
        with open(os.path.join(products_path, filename), 'w') as file:
            for product_name in func_dict[key]:
                fieldnames1=['product_id','product_size','product_price','product_name']
                writer = csv.DictWriter(file, fieldnames=fieldnames1)
                writer.writeheader()
                for row in func_dict[key]:
                    entry = f"{row['product_id']},{row['product_size']},{row['product_price']},{row['product_name']}"
                    #print(f"{row['product_id']},{row['product_size']},{row['product_price']},{row['product_name']}")
                    writer.writerow(entry)

                
                
    # with open('people200.csv', mode='w') as file:
    #     #it is usual to hardset the filenames, as this defines the column order
    #     fieldnames = [' phone', 'name']
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writeheader()
    #     for row in lineslist:
    #         writer.writerow(row)

####################################################################################################
####################################################################################################
###     IMPORT PRODUCT_TXT
####################################################################################################
####################################################################################################

def import_products(): #returns food_dict
    global choice_list
    choice_list = []  # ['Drinks', 'Cold food', 'Hot food']

    global food_dict
    food_dict = dict()

    # sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    print("Current Directory: ", current_path)
    print("Parent Directory: ", parent_path)
    products_file = os.path.join(current_path, "products", "hot_food.txt")
    products_path = os.path.join(current_path, "products")

    for index, filename in enumerate(os.listdir(products_path)):
        print("printing filename", index, filename)
        # starting with an empty list, populating choicelist based on filenames, stripping out .txt
        clean_name = filename.strip(".txt")
        choice_list.append(clean_name)
        globals()[filename.strip(".txt")] = []

        #print(f"This is the choise list :{choice_list}")
        #category_new[index] = filename.strip(".txt")
        (os.path.join(products_path, filename))
        with open(os.path.join(products_path, filename), 'r') as file:
            globals()[clean_name] = file.read().splitlines(0)
            #print(f"Final filename contents of file: {clean_name}: {globals()[clean_name]}")
            food_dict[clean_name] = globals()[clean_name]
    return food_dict


# module below used to presist data by exporting food_dict into txt files in products folder
####################################################################################################
####################################################################################################
###     EXPORT PRODUCT_TXT
####################################################################################################
####################################################################################################
def export_products(courier_dict=[{"Dummy Order List": "I don't know"}]):
    # sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    products_path = os.path.join(current_path, "products")

    # getting the latest choice_list from food_dict
    choice_list = list(food_dict.keys())

    for key in food_dict.keys():
        globals()[key]
        filename = key + ".txt"
        with open(os.path.join(products_path, filename), 'w') as file:
            for product_name in food_dict[key]:
                file.write(product_name + '\n')


def import_couriers(): #returns courier_dict
    couriers_list = []
    courier_dict = {}

    # sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    couriers_path = os.path.join(current_path, "couriers")

    for index, filename in enumerate(os.listdir(couriers_path)):
        print("printing filename with index ", index, filename)
        # starting with an empty list, populating choicelist based on filenames, stripping out .txt
        clean_name = filename.strip(".txt")
        couriers_list.append(clean_name)
        globals()[filename.strip(".txt")] = []

        #print(f"This is the choise list :{choice_list}")
        #category_new[index] = filename.strip(".txt")
        (os.path.join(couriers_path, filename))
        with open(os.path.join(couriers_path, filename), 'r') as file:
            globals()[clean_name] = file.read().splitlines(0)
            #print(f"Final filename contents of file: {clean_name}: {globals()[clean_name]}")
            courier_dict[clean_name] = globals()[clean_name]
    print(
        f"Final filename contents of file: {couriers_list[-1]}: {globals()[couriers_list[-1]]}")
    return courier_dict


def export_couriers(courier_dict=[{"Dummy Order List": "I don't know"}]):
    # sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    couriers_path = os.path.join(current_path, "couriers")

    # getting the latest choice_list from food_dict
    courier_list = list(courier_dict.keys())

    for key in courier_dict.keys():
        globals()[key]
        filename = key + ".txt"
        with open(os.path.join(couriers_path, filename), 'w') as file:
            for product_name in courier_dict[key]:
                file.write(product_name + '\n')


def import_orders(): #returns orders_list: A list of dicts
    global orders_list
    orders_list = []

    # json_filename = f'ordertaken_{dt_obj: %Y%m%d_%H%M}'#'creating timestamp name
    json_filename = "orders"
    print(json_filename)

    folder = Path('orders')
    print(folder)
    jsonpath = folder / f"{json_filename}.json"
    print(jsonpath)

    # sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)

    orders_path = os.path.join(current_path, "orders")

    (os.path.join(orders_path, json_filename))
    with open(os.path.join(orders_path, f"{json_filename}.json"), 'r') as file:
        order_list = json.load(file)
    print(f"Order_list: {order_list}")
    return order_list


def export_orders(orders_list=[{"Dummy Order List": "I don't know"}]):
    # json_filename = f'ordertaken_{dt_obj: %Y%m%d_%H%M}'#'creating timestamp name
    json_filename = "orders"
    #print(json_filename)

    folder = Path('orders')
    #print(folder)
    jsonpath = folder / f"{json_filename}.json"
    #print(jsonpath)

    # this is writing to json file!!!
    folder.mkdir(exist_ok=True)
    jsonpath.write_text(json.dumps(orders_list))
