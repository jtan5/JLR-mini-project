from enum import unique
import os
import copy
import sys
import time
import random
from pathlib import Path
from datetime import datetime
# from traceback import print_list
# from unicodedata import category
# import phonenumbers
# from phonenumbers import carrier
# from phonenumbers.phonenumberutil import number_type
from source.functions import yes_no_catcher, print_dict, print_dynamic_list, print_list_of_dict, selection_catcher, blank_catcher, price_catcher, phone_catcher, int_catcher, selection_catcher_dict
from source.art import food_drink_art, order_art, courier_art, area_art, new_product_art, new_courier_art
from source.order_menu import print_order, create_new_order, changing_order_status

os.path.abspath(__file__)
current_path = os.getcwd()
print(current_path)
sys.path.append(os.path.dirname(__file__))
print(sys.path)
import access_func as af


####################################################################################################
####################################################################################################
###     MAIN MENU
####################################################################################################
####################################################################################################
def main_menu():
 
    os.system('clear')
    print(food_drink_art)
    print("Welcome to the Bootcamp Cafe Setup Page\n")
    main_menu_list = ['Quit', 'Go to products', 'Go to couriers','Go to orders']
    print_dynamic_list(main_menu_list)
    try:
        choice = int(input("Please enter a valid option as listed above\n"))
        if choice == 0:
            print("You have decided to quit the program\n")
            return choice
        if choice == 1: #products
            return product_menu()
        if choice ==2: #couriers
            return courier_menu()
            #return print(10)
        if choice ==3: #orders
            return order_menu()
        if choice >= len(main_menu_list):
            os.system('clear')
            return main_menu()
    except ValueError:
        os.system('clear')
        print('You have entered a non-numerical / blank value\n\n\n')
        print("Menu will load shortly...")
        time.sleep(2)
        return main_menu()
        
####################################################################################################
####################################################################################################
###     PRODUCT MENU
####################################################################################################
####################################################################################################
    
def product_menu():

    unique_list_of_dict = af.import_product_db() 
    category = "product"
    unique_list = ['Main Menu', 
                   f'Print {category.title()} List', 
                   f'Create New {category.title()}',          
                   f'UPDATE Exising {category.title()}', 
                   f'DELETE Existing {category.title()}']

    os.system('clear')
    print(f"This is the {category}s menu\n")
    choice = selection_catcher(unique_list,message = "PRODUCT MENU\n",art=food_drink_art)
    if choice == 0: #returning to main menu
        return main_menu()
    if choice == 1: #printing items
        os.system('clear')
        print_list_of_dict(unique_list_of_dict)
        input("Press any key to go back\n")
        return product_menu()

    if choice ==2:  #adding item
        add_item = new_item(unique_list_of_dict,category)
        if add_item is True:
            print(f"{category.title()} has been added successfully")
        else:
            print(f"Whoops... unable to add new {category}, please check database connection and try again")
        input("Press any key to go back\n")
        return product_menu()

    if choice ==3:  #editing item
        update_product=update_many_items(unique_list_of_dict, category)
        if update_product is True:
            print(f"{category.title()} has been added successfully")
        else:
            print(f"Whoops... unable to add new {category}, please check database connection and try again")
        input("Press any key to go back\n")
        return product_menu()

    if choice ==4:  #deleting item
        delete_product = delete_item(unique_list_of_dict,category)
        if delete_product is True:
            print(f"{category.title()} has been added successfully")
        else:
            print(f"Whoops... unable to add new {category}, please check database connection and try again")
        input("Press any key to go back\n")
        return product_menu()


####################################################################################################
####################################################################################################
###     COURIER MENU
####################################################################################################
####################################################################################################
def courier_menu():

    unique_list_of_dict = af.import_courier_db() 
    category = "courier"
    unique_list = ['Main Menu', f'Print {category.title()} List', f'Create New {category.title()}',
          f'UPDATE Exising {category.title()}', f'DELETE Existing {category.title()}']

    os.system('clear')
    print(f"This is the {category}s menu\n")
    choice = selection_catcher(unique_list,message = "COURIER MENU",art=courier_art)
    if choice == 0: #returning to main menu
        return main_menu()
    if choice == 1: #printing items
        os.system('clear')
        print_list_of_dict(unique_list_of_dict)
        input("Press any key to go back\n")
        return courier_menu()

    if choice ==2:  #adding item
        add_item = new_item(unique_list_of_dict,category)
        if add_item is True:
            print(f"{category.title()} has been added successfully")
        else:
            print(f"Whoops... unable to add new {category}, please check database connection and try again")
        input("Press any key to go back\n")
        return courier_menu()
        

    if choice ==3:  #editing item
        update_product=update_many_items(unique_list_of_dict, category)
        if update_product is True:
            print(f"{category.title()} has been added successfully")
        else:
            print(f"Whoops... unable to add new {category}, please check database connection and try again")
        input("Press any key to go back\n")
        return courier_menu()

    if choice ==4:  #deleting item
        delete_product = delete_item(unique_list_of_dict,category)
        if delete_product is True:
            print(f"{category.title()} has been added successfully")
        else:
            print(f"Whoops... unable to add new {category}, please check database connection and try again")
        input("Press any key to go back\n")
        return courier_menu()

####################################################################################################
####################################################################################################
###     ORDER MENU
####################################################################################################
####################################################################################################
def order_menu():
    #customer list
    os.system('clear')
    print(order_art)
    category = "order"
    print(f"This is the {category}s menu\n")
    unique_list = ['Main Menu', f'Print {category.title()} List', f'Create New {category.title()}',
          f'UPDATE {category.title()} Status', f'DELETE Existing {category.title()}']
    os.system('clear')
    print(f"This is the {category}s menu\n")
    choice = selection_catcher(unique_list,message = "ORDERS MENU",art=order_art)
    if choice == 0: #returning to main menu
        return main_menu()
    
    if choice == 1: #printing items
        os.system('clear')
        print_order()
        input("Press any key to go back\n")
        return order_menu()

    if choice ==2:  #adding item
        add_item = create_new_order()
        if add_item is True:
            print(f"{category.title()} has been added successfully")
        else:
           print(f"Whoops... unable to add new {category}, please check database connection and try again")
        input("Press any key to go back\n")
        return order_menu()

    if choice ==3:  #editing item
        changing_order_status()
        input("Press any key to go back\n")
        return order_menu()

    if choice ==4:  #deleting item
        #delete_menu()
        return order_menu()

    if choice >= len(unique_list):
        os.system('clear')
        return order_menu()



####################################################################################################
####################################################################################################
###     APPEND MENU - PRODUCT OR COURIER OR ORDER
####################################################################################################
####################################################################################################

def new_item(unique_list_of_dict,category:str): #category = "product", "courier"

    os.system('clear')
    if category == "product":
        art = new_product_art
        print(art)
        print_list_of_dict(unique_list_of_dict)
        new_item_name, new_item_stock, new_item_price, product_size = new_product_questions()#write new items to database
        af.insert_product(new_item_name,new_item_stock,new_item_price, product_size)
        
    else: 
        art = new_courier_art
        print(art)
        print_list_of_dict(unique_list_of_dict)
        new_item_name, new_item_number, new_item_capacity = new_courier_questions()#write new items to database
        af.insert_courier(new_item_name, new_item_number, new_item_capacity)

    return True



####################################################################################################
####################################################################################################
###     NEW PRODUCT QUESTION
####################################################################################################
####################################################################################################
def new_product_questions():
    #os.system("clear")
    print(new_product_art)
    question = "Please enter name of product you would like to add"
    new_item_name = blank_catcher(question)
    question = "Please enter stock amount"
    new_item_stock = int_catcher(question)
    question = "Please enter price of product you would like to add"
    new_item_price = price_catcher(question)
    question = "Please enter product size"
    product_size = blank_catcher(question)

    return new_item_name, new_item_stock, new_item_price, product_size
####################################################################################################
####################################################################################################
###     NEW COURIER QUESTION
####################################################################################################
####################################################################################################
def new_courier_questions():
    #os.system("clear")
    print(new_courier_art)
    question = "Please enter courier name"
    new_item_name = blank_catcher(question)
    question = "Please enter courier number"
    new_item_number = phone_catcher()
    areas = ["Greater London", "West Midlands", "District-9", "Area-51"]
    question = "Please enter the servicing area for deliveries"
    servicing_area = areas[selection_catcher(areas,question,area_art)]
    return new_item_name, new_item_number, servicing_area


####################################################################################################
####################################################################################################
###     UPDATE MANY ITEMS
####################################################################################################
####################################################################################################
    
def update_many_items(unique_list_of_dict: list,category):
    seq = False
    new_item_list = []
    while seq is False:
        new_item_dict = update_item(unique_list_of_dict, category)
        new_item_copy = copy.deepcopy(new_item_dict)
        new_item_list.append(new_item_copy)
        os.system("clear")
        question = f"Would you like to update another {category}?"
        update_another = yes_no_catcher(question)
        if update_another =="No":
            seq = True
    print(new_item_list)
    upload_product = af.change_item(new_item_list,category)
    return True
    

####################################################################################################
###     UPDATE ITEM
####################################################################################################
def update_item(unique_list_of_dict:list,category:str):
    #first get product_id
    update_product_dict= {}
    #unique_list_of_dict = af.import_product_db() 
    question = f"Please select {category} you would like to update"
    choice = selection_catcher_dict(unique_list_of_dict,question,food_drink_art)
    
    #saving that product id into update_product variable
    update_product_dict = unique_list_of_dict[choice]
    #product_id = update_product_dict["product_id"]
    print(f"The following {category} has been selected")
    print_dict(update_product_dict)
    #then get product_name, product_size, unit_price, stock_number
    string_for_item_id = f"{category}_id"

    for k, v in update_product_dict.items():
        if k != string_for_item_id:
            question=(f"Would you like to change {k} value? It is currently {v}\nPress Enter to skip update")
            new_entry = blank_catcher(question,allow_blanks=True)
            if new_entry != "":
                update_product_dict[k] = new_entry
    print(f"The selected {category} will be updated as follows:")
    print_dict(update_product_dict)
    return update_product_dict    

def delete_item(list_of_dict:list,category:str):
    item_id = 1
    pass
    #first get product_id
    
    #return product_name, product_size, unit_price, stock_number
    
    