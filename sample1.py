import os
import json

import json
from pathlib import Path


def import_orders():
    
    #json_filename = f'ordertaken_{dt_obj: %Y%m%d_%H%M}'#'creating timestamp name
    json_filename = "orders"
    #print(json_filename)

    folder = Path('orders')
    #print(folder)
    jsonpath = folder / (json_filename + ".json")
    #print(jsonpath)
    
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
        order_list = json.load(file)
    print(f"Order_list: {order_list}")


import_orders()