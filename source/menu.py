import os
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
from .functions import print_dynamic_list, print_list_of_dict, print_list_of_dict_selection, selection_catcher, selection_catcher_dict, blank_catcher, price_catcher, phone_catcher, int_catcher
from .art import food_drink_art, order_art, courier_art, area_art, customer_art, new_product_art, new_courier_art, new_order_art, new_customer_art
from .order_menu import print_order, create_new_order, changing_order_status

os.path.abspath(__file__)
current_path = os.getcwd()
print(current_path)
sys.path.append(os.path.dirname(__file__))
print(sys.path)
import access_func as af



def main_menu():
 
    os.system('clear')
    print(food_drink_art)
    print("Welcome to the Bootcamp Cafe Setup Page\n")
    main_menu_list = ['Quit', 'View all products', 'View all couriers','View all orders']
    print_dynamic_list(main_menu_list)
    try:
        choice = int(input("Please enter a valid option as listed above\n"))
        # if choice == 99:
        #     main_menu()
        if choice == 0:
            print("You have decided to quit the program\n")
            return choice
        if choice == 1: #products
            product_menu()
            return choice
        if choice ==2: #couriers
            courier_menu()
            return choice
        if choice ==3: #orders
            order_menu()
            return choice
        if choice >= len(main_menu_list):
            os.system('clear')
            main_menu()
    except ValueError:
        os.system('clear')
        print('You have entered a non-numerical / blank value\n\n\n')
        print("Menu will load shortly...")
        time.sleep(2)
        main_menu()
        
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
    choice = selection_catcher(unique_list,message = "PRODUCT MENU\n",include_99=0,art=food_drink_art)
    if choice == 0: #returning to main menu
        main_menu()
    if choice == 1: #printing items
        os.system('clear')
        print_list_of_dict(unique_list_of_dict)
        input("Press any key to go back to the main menu\n")
        main_menu()
        return choice
    if choice ==2:  #adding item
        new_item(unique_list_of_dict,category)
        main_menu()
        return choice
    if choice ==3:  #editing item
        update_product()
        main_menu()
        return choice
    if choice ==4:  #deleting item
        delete_product()
        main_menu()
        return choice

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
    choice = selection_catcher(unique_list,message = "COURIER MENU",include_99=0,art=courier_art)
    if choice == 0: #returning to main menu
        main_menu()
    if choice == 1: #printing items
        os.system('clear')
        print_list_of_dict(unique_list_of_dict)
        input("Press any key to go back to the main menu\n")
        main_menu()
        return choice
    if choice ==2:  #adding item
        new_item(unique_list_of_dict,category)
        main_menu()
        return choice
    if choice ==3:  #editing item
        update_product()
        main_menu()
        return choice
    if choice ==4:  #deleting item
        delete_product()
        main_menu()
        return choice
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
    choice = selection_catcher(unique_list,message = "ORDERS MENU",include_99=0,art=order_art)
    if choice == 0: #returning to main menu
        main_menu()
    if choice == 1: #printing items
        os.system('clear')
        print_order()
        main_menu()
        return choice
    if choice ==2:  #adding item
        create_new_order()
        main_menu()
        return choice
    if choice ==3:  #editing item
        changing_order_status()
        main_menu()
        return choice
    if choice ==4:  #deleting item
        #delete_menu()
        main_menu()
        return choice
    if choice >= len(unique_list):
        os.system('clear')
        main_menu()



####################################################################################################
####################################################################################################
###     APPEND MENU - PRODUCT OR COURIER OR ORDER
####################################################################################################
####################################################################################################

def new_item(unique_list_of_dict,category:str): #category = "product", "courier", "order"

    os.system('clear')
    if category == "product":
        art = new_product_art
        print(art)
        print_list_of_dict(unique_list_of_dict)
        new_item_name, new_item_stock, new_item_price = new_product_questions()#write new items to database
        af.insert_product(new_item_name,new_item_stock,new_item_price)
        
    elif category == "courier":
        art = new_courier_art
        print(art)
        print_list_of_dict(unique_list_of_dict)
        new_item_name, new_item_number, new_item_capacity = new_courier_questions()#write new items to database
        af.insert_courier(new_item_name, new_item_number, new_item_capacity)
    else:
        art = order_art
        print(art)
        print_list_of_dict(unique_list_of_dict)
        
        #write new items to database
        #insert_order(name, address, postcode, servicing_area)

    input("Press any key to go back to the main menu\n")
    main_menu()


####################################################################################################
####################################################################################################
###     NEW PRODUCT QUESTION
####################################################################################################
####################################################################################################
def new_product_questions():
    question = "Please enter name of product you would like to add"
    new_item_name = blank_catcher(question)
    question = "Please enter stock amount"
    new_item_stock = int_catcher(question)
    question = "Please enter price of product you would like to add"
    new_item_price = price_catcher(question)
    return new_item_name, new_item_stock, new_item_price
####################################################################################################
####################################################################################################
###     NEW COURIER QUESTION
####################################################################################################
####################################################################################################
def new_courier_questions():
    question = "Please enter courier name"
    new_item_name = blank_catcher(question)
    question = "Please enter courier number"
    new_item_number = phone_catcher()
    areas = ["Greater London", "West Midlands", "District-9", "Area-51"]
    question = "Please enter the servicing area for deliveries"
    servicing_area = areas[selection_catcher(areas,question,0,area_art)]
    return new_item_name, new_item_number, servicing_area



    
def update_product():
    pass

def delete_product():
    pass

        
def random_courier(courier_list_of_dict):
    courier_list = list(courier_list_of_dict.keys())
    choice = selection_catcher(courier_list,message = "Please select the servicing area closest to your delivery location\n",include_99=1)
    selection = courier_list[choice]
    print(f"You have selected: {selection}")
    time.sleep(1)
    print(f"All couriers from {selection} listed below:\n")
    print_dynamic_list(courier_list_of_dict[selection])
    os.system("clear")
    print("Assigning a courier to your order...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    os.system("clear")
    print("Courier found...")
    time.sleep(1)
    os.system("clear")
    random_courier = random.randint(0, len(courier_list_of_dict[selection]))
    #print (f"Random courier: {random_courier}")
    print(f"Thank you for your order... \n\n\nCourier {courier_list_of_dict[selection][random_courier]} from {selection} has been assigned to your order.")
    return f"{selection},{courier_list_of_dict[selection][random_courier]}"



    
