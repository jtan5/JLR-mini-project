import os
import sys
import time
import random
from pathlib import Path
from datetime import datetime
from traceback import print_list
from unicodedata import category
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
 

os.path.abspath(__file__)
current_path = os.getcwd()
print(current_path)
sys.path.append(os.path.dirname(__file__))
print(sys.path)
import access_func as af
from db_functions import execute_query, execute_query2, insert_product, insert_courier, read_from_db, get_unique_id

#these will automatically populate once the program runs
#product_dict = af.import_products()#      #function returns product_dict
product_dict = af.import_product_db()  
courier_dict = af.import_couriers()    #function returns couriers dict
orders_list = af.import_orders()        #function returns orders_list



# Images
food_drink_art = """
  ;)( ;
 :----:     o8Oo./
C|====| ._o8o8o8Oo_.
 |    |  \========/
 `----'   `------'
"""
courier_art = """
   -           __
 --          ~( @\ \\\\
---   _________]_[__/_>________
     /  ____ \ <>     |  ____  \\
    =\_/ __ \_\_______|_/ __ \__]
________(__)_____________(__)____
"""
order_art = '''
                  .----.
      .---------. | == |
      |.-"""""-.| |----|
      ||  X X  || | == |
      ||   _   || |----|
      |'-.....-'| |::::|
      `"")---(""` |___.|
     /:::::::::::\" _  "
    /:::=======:::\`\`\\
    `"""""""""""""`  '-'
'''
area_art = '''
        _____
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
    `'-._____.-'
'''
new_product_art = '''
 ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗    ███╗   ██╗███████╗██╗    ██╗    ██████╗ ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗████████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝    ████╗  ██║██╔════╝██║    ██║    ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝
██║     ██████╔╝█████╗  ███████║   ██║   █████╗      ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██████╔╝██████╔╝██║   ██║██║  ██║██║   ██║██║        ██║   
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝      ██║╚██╗██║██╔══╝  ██║███╗██║    ██╔═══╝ ██╔══██╗██║   ██║██║  ██║██║   ██║██║        ██║   
╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗    ██║ ╚████║███████╗╚███╔███╔╝    ██║     ██║  ██║╚██████╔╝██████╔╝╚██████╔╝╚██████╗   ██║   
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝  ╚═════╝   ╚═╝   
'''
new_courier_art = '''
███████╗███████╗████████╗██╗   ██╗██████╗     ███╗   ██╗███████╗██╗    ██╗     ██████╗ ██████╗ ██╗   ██╗██████╗ ██╗███████╗██████╗ 
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗    ████╗  ██║██╔════╝██║    ██║    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██║██╔════╝██╔══██╗
███████╗█████╗     ██║   ██║   ██║██████╔╝    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║     ██║   ██║██║   ██║██████╔╝██║█████╗  ██████╔╝
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝     ██║╚██╗██║██╔══╝  ██║███╗██║    ██║     ██║   ██║██║   ██║██╔══██╗██║██╔══╝  ██╔══██╗
███████║███████╗   ██║   ╚██████╔╝██║         ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╗╚██████╔╝╚██████╔╝██║  ██║██║███████╗██║  ██║
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝         ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝
'''
new_order_art = '''
 ██████╗██████╗ ███████╗ █████╗ ████████╗███████╗    ███╗   ██╗███████╗██╗    ██╗     ██████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝    ████╗  ██║██╔════╝██║    ██║    ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║     ██████╔╝█████╗  ███████║   ██║   █████╗      ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝
██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██╔══╝      ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗██║  ██║   ██║   ███████╗    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
 '''
 


def print_dynamic_list(selection_list):
    if selection_list is None:
        selection_list = ["DEBUG LIST", "LIST_ID1","LIST_ID2"]
    for index, val in enumerate(selection_list):
        print(f"[{index}] - {val}")

def print_dict(func_dict):
    print("\n".join(f"{k:<20}{v}\n" for k, v in func_dict.items()))
    input("Press any key to go back to the main menu\n")
    
def print_dict_complex(func_dict):
    for key, value in func_dict.items():
        print(f"{key:<20}")
        print_list_of_dict_non_order(value)
        print()
        print()
    input("Press any key to go back to the main menu\n")
    
def print_list_of_dict_non_order(func_list):
    for i, _ in enumerate(func_list): #[ {order1}, {order2} , {order3}]
        #print(f"This is order {i+1} of {len(func_list)}")
        print("\t".join(f"{k}:{v}" for k, v in func_list[i].items()))

            
def print_list_of_dict(func_list): #use for order
    for i, _ in enumerate(func_list): #[ {order1}, {order2} , {order3}]
        print(f"This is order {i+1} of {len(func_list)}")
        print("\n".join(f"{k:<25}{v}\t" for k, v in func_list[i].items()))
        print()
        if i+1 ==len(func_list):
            print("This is the last record")
            input("Press any key to go back to the main menu\n")
        else:
            input("Press any key to see next order\n")


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

    unique_dict = af.import_product_db() 
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
        print_list_of_dict_non_order(unique_dict)
        input("Press any key to go back to the main menu\n")
        main_menu()
        return choice
    if choice ==2:  #adding item
        new_item(unique_dict,category)
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




def courier_menu():

    unique_dict = af.import_courier_db() 
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
        print_list_of_dict_non_order(unique_dict)
        input("Press any key to go back to the main menu\n")
        main_menu()
        return choice
    if choice ==2:  #adding item
        new_item(unique_dict,category)
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
    os.system('clear')
    print(order_art)
    category = "order"
    print(f"This is the {category}s menu\n")
    unique_list = ['Main Menu', f'Print {category.title()} List', f'Create New {category.title()}',
          f'UPDATE Exising {category.title()}', f'DELETE Existing {category.title()}']
    os.system('clear')
    print(f"This is the {category}s menu\n")
    choice = selection_catcher(unique_list,message = "ORDERS MENU",include_99=0,art=order_art)
    if choice == 0: #returning to main menu
        main_menu()
    if choice == 1: #printing items
        os.system('clear')
        print_list_of_dict(orders_list)
        main_menu()
        return choice
    if choice ==2:  #adding item
        new_order(orders_list,category)
        main_menu()
        return choice
    if choice ==3:  #editing item
        update_menu()
        main_menu()
        return choice
    if choice ==4:  #deleting item
        delete_menu()
        main_menu()
        return choice
    if choice >= len(unique_list):
        os.system('clear')
        main_menu()



####################################################################################################
####################################################################################################
###     APPEND MENU - PRODUCT OR COURIER
####################################################################################################
####################################################################################################

def new_item(unique_dict,category:str): #category = "product", "courier", "order"

    os.system('clear')
    if category == "product":
        art = new_product_art
        print(art)
        print_list_of_dict_non_order(unique_dict)
        new_item_name, new_item_size, new_item_price = new_product_questions()#write new items to database
        insert_product(new_item_name,new_item_size,new_item_price)
        
    elif category == "courier":
        art = new_courier_art
        print(art)
        print_list_of_dict_non_order(unique_dict)
        new_item_name, new_item_number, new_item_capacity = new_courier_questions()#write new items to database
        insert_courier(new_item_name, new_item_number, new_item_capacity)
    else:
        art = order_art
        print(art)
        print_list_of_dict_non_order(unique_dict)
        number = get_unique_id(new_item_name,"product")
        print (number)

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
    question = "Please enter size of product you would like to add\nEnter N/A if not applicable"
    new_item_size = blank_catcher(question)
    question = "Please enter price of product you would like to add"
    new_item_price = price_catcher(question)
    return new_item_name, new_item_size, new_item_price
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
####################################################################################################
####################################################################################################
###     NEW ORDER QUESTION
####################################################################################################
####################################################################################################
def new_order_questions():
    question = "Please enter courier name"
    new_item_name = blank_catcher(question)
    question = "Please enter courier number"
    new_item_number = int_catcher(question)
    question = "Please enter max order capacity per order"
    new_item_capacity = int_catcher(question)
    return new_item_name, new_item_number, new_item_capacity
####################################################################################################
####################################################################################################
###     APPEND MENU - ORDER
####################################################################################################
####################################################################################################
def new_order(orders_list,category: str = None): #use for orders only
    os.system('clear')
    print(new_order_art)
    new_order = {}
    new_order["customer_name"] = input("Please enter customer name\n")
    new_order["customer_address_1"] = input("Please enter first line address\n")
    new_order["customer_address_2"] = input("Please enter second line address\nEg: London, Amsterdam, Bogota\n")
    new_order["customer_postcode"] = input("Please enter customer postcode\n")
    os.system('clear')
    print_dynamic_list(courier_dict) #give you a selection to select the area (corresponds to filename)
    new_order["courier_name"] = random_courier(courier_dict)
    dt_obj = datetime.now()
    new_order["order_time"] = f'ordertaken_{dt_obj: %Y%m%d_%H%M}', #'creating timestamp
    new_order["status"] = "new"
    #saving the new_order into orders_list
    orders_list.append(new_order)
    af.export_orders(orders_list)
    print(f"{category.title()} has been successfully updated")
    input("Press any key to return to main menu\n")
    main_menu()


    
def update_product():
    pass

def delete_product():
    pass

        
def random_courier(courier_dict):
    courier_list = list(courier_dict.keys())
    choice = selection_catcher(courier_list,message = "Please select the servicing area closest to your delivery location\n",include_99=1)
    selection = courier_list[choice]
    print(f"You have selected: {selection}")
    time.sleep(1)
    print(f"All couriers from {selection} listed below:\n")
    print_dynamic_list(courier_dict[selection])
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
    random_courier = random.randint(0, len(courier_dict[selection]))
    #print (f"Random courier: {random_courier}")
    print(f"Thank you for your order... \n\n\nCourier {courier_dict[selection][random_courier]} from {selection} has been assigned to your order.")
    return f"{selection},{courier_dict[selection][random_courier]}"


####################################################################################################
####################################################################################################
###     SELECTION CATCHER
####################################################################################################
####################################################################################################
def selection_catcher(func_list: list,message: str,include_99=1,art=None):
    choice = 50
    while choice >=len(func_list):
        #os.system("clear")
        print(art)
        print_dynamic_list(func_list)
        if include_99 == 1:
            print("[99] - Return to main menu")
        else:
            pass #no special menu to add
        print(message)
        try: 
            choice = int(input("Please enter a valid option as listed above\n"))
        except ValueError:
            os.system('clear')
            print('You have entered a non-numerical / blank value\n\n\n')
            print("Menu will load shortly...")
            time.sleep(2)
            
    if choice == 99:
        main_menu()
    else:
        return choice
    
####################################################################################################
####################################################################################################
###     BLANK CATCHER
####################################################################################################
####################################################################################################
def blank_catcher(message: str):
    new_item = ""
    while new_item == "": #no blank catcher
        new_item = input(f"{message}\n")
    return new_item

####################################################################################################
####################################################################################################
###     PRICE CATCHER
####################################################################################################
####################################################################################################
def price_catcher(message: str):
    new_item = ""
    while new_item == "": #no blank catchertry: 
        try:
            new_item = float(input(f"{message}\n"))
        except ValueError:
            os.system('clear')
            print('You have entered a non-numerical / blank value\n\n\n')
            print("Menu will load shortly...")
            time.sleep(2)
    return new_item

####################################################################################################
####################################################################################################
###     INT CATCHER
####################################################################################################
####################################################################################################
def int_catcher(message: str):
    new_item = ""
    while new_item == "": #no blank catchertry: 
        try:
            new_item = int(input(f"{message}\n"))
        except ValueError:
            os.system('clear')
            print('You have entered a non-numerical / blank value\n\n\n')
            print("Menu will load shortly...")
            time.sleep(2)
    return new_item
####################################################################################################
####################################################################################################
###     PHONE CATCHER
####################################################################################################
####################################################################################################
def phone_catcher():
    try:
        #number = "+447939418683"
        number = input("Please enter courier mobile phone number by beginning with the country code\neg: +447123456789\n")
        mobile_number = carrier._is_mobile(number_type(phonenumbers.parse(number)))
    except Exception as e:
        print(f"Error with phone number, error code: {e}")
        time.sleep(2)
        phone_catcher()
    if mobile_number is True:
        number = number.replace(" ","")
        print(number)
        return number
    else:
        print(f"The phone number you have entered is not a valid mobile number, please re-enter\nEntry screen will reload shortly...")
        time.sleep(2)
        phone_catcher()
####################################################################################################
####################################################################################################
###     SERVICING AREA CATCHER
####################################################################################################
####################################################################################################
def servicing_area_catcher():
    areas = ["Greater London", "West Midlands", "District-9", "Area-51"]
    print_list(areas)
    while new_item == "": #no blank catchertry: 
        try:
            new_item = float(input(f"{message}\n"))
        except ValueError:
            os.system('clear')
            print('You have entered a non-numerical / blank value\n\n\n')
            print("Menu will load shortly...")
            time.sleep(2)
    return new_item