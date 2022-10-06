import os
import json

from pathlib import Path
from datetime import datetime
 
dt_obj = datetime.now()

def import_orders():
    #global orders_list
    #orders_list = []
    
    #global orders_dict
    #orders_dict = {}

    # sample_order_1 = {
    #     "customer_name": "John",
    #     "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    #     "customer_phone": "0789887334",
    #     "courier": 2,
    #     "order_time" : f'ordertaken_{dt_obj: %Y%m%d_%H%M}', #'creating timestamp
    #     "status": "preparing"
    #     }
    # sample_order_2 = {
    # "customer_name": "Henry",
    # "customer_address": "Unit 2, 15 Main Street, LONDON, WH1 2RR",
    # "customer_phone": "0789887334",
    # "courier": 3,
    # "order_time" : f'ordertaken_{dt_obj: %Y%m%d_%H%M}', #'creating timestamp
    # "status": "ready"
    # }
    # orders_list.append(sample_order_1)
    # orders_list.append(sample_order_2)
    # print(orders_list)
    
    #json_filename = f'ordertaken_{dt_obj: %Y%m%d_%H%M}'#'creating timestamp name
    json_filename = "orders"
    print(json_filename)

    folder = Path('order')
    print(folder)
    jsonpath = folder / (json_filename + ".json")
    print(jsonpath)
    
    #jsonpath.load(json)
    
    # #this is writing to json file!!!
    # folder.mkdir(exist_ok=True)
    # jsonpath.write_text(json.dumps(orders_list))
                
    #sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)

    orders_path = os.path.join(current_path, "orders")


    (os.path.join(orders_path, json_filename))
    with open(os.path.join(orders_path, json_filename + ".json"), 'r') as file:
        order_list_10 = json.load(file)
    print(f"Order_list: {order_list_10}")
        #globals()[clean_name] = file.read().splitlines(0)
        #print(f"Final filename contents of file: {clean_name}: {globals()[clean_name]}")
        #orders_dict[clean_name] = globals()[clean_name]
    #print(f"Final filename contents of file: {orders_list[-1]}: {globals()[orders_list[-1]]}")
    
import_orders()