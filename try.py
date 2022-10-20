from source import menu
from source.functions import blank_catcher, selection_catcher, selection_catcher_dict, print_dict, yes_no_catcher
from source.art import food_drink_art
from source import access_func as af

import os
import time
import copy


# unique_list_of_dict = af.import_product_db() 
# category = "product"

# def update_many_items(unique_list_of_dict: list,category):
#     seq = False
#     new_item_list = []
#     while seq is False:
#         new_item_dict = update_item(unique_list_of_dict, category)
#         new_item_copy = copy.deepcopy(new_item_dict)
#         new_item_list.append(new_item_copy)
#         os.system("clear")
#         question = f"Would you like to update another {category}?"
#         update_another = yes_no_catcher(question)
#         if update_another =="No":
#             seq = True
#     print(new_item_list)
    
#     upload_product = af.change_item(new_item_list,category)
    

    
# def update_item(unique_list_of_dict:list,category:str):
#     #first get product_id
#     update_product_dict= {}
#     #unique_list_of_dict = af.import_product_db() 
#     question = f"Please select {category} you would like to update"
#     choice = selection_catcher_dict(unique_list_of_dict,question,food_drink_art)
    
#     #saving that product id into update_product variable
#     update_product_dict = unique_list_of_dict[choice]
#     #product_id = update_product_dict["product_id"]
#     print(f"The following {category} has been selected")
#     print_dict(update_product_dict)
#     #then get product_name, product_size, unit_price, stock_number
#     string_for_item_id = f"{category}_id"

#     for k, v in update_product_dict.items():
#         if k != string_for_item_id:
#             question=(f"Would you like to change {k} value? It is currently {v}\nPress Enter to skip update")
#             new_entry = blank_catcher(question,allow_blanks=True)
#             if new_entry != "":
#                 update_product_dict[k] = new_entry
#     print(f"The selected {category} will be updated as follows:")
#     print_dict(update_product_dict)
#     return update_product_dict    
    
    
# update_many_items(unique_list_of_dict, category)
# #af.test_query()

menu.save_and_exit()
