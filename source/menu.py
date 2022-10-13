import os
import sys
import time
import random
from pathlib import Path
from datetime import datetime
from traceback import print_list
 

os.path.abspath(__file__)
current_path = os.getcwd()
print(current_path)
sys.path.append(os.path.dirname(__file__))
print(sys.path)
import access_func as af

#these will automatically populate once the program runs
#food_dict = af.import_products()#      #function returns food_dict
food_dict = af.import_product_csv()  
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
        print("\n".join(f"{k:<25}{v}" for k, v in func_list[i].items()))
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

    #food_dict = af.import_products()
    unique_dict = food_dict
    unique_string = "product"
    unique_list = ['Main Menu', 
                   f'Print {unique_string.title()} List', 
                   f'Create New {unique_string.title()}',          
                   f'UPDATE Exising {unique_string.title()}', 
                   f'DELETE Existing {unique_string.title()}']

    os.system('clear')
    print(f"This is the {unique_string}s menu\n")
    choice = selection_catcher(unique_list,message = "PRODUCT MENU\n",include_99=0,art=food_drink_art)
    if choice == 0: #returning to main menu
        main_menu()
    if choice == 1: #printing items
        os.system('clear')
        print_dict_complex(unique_dict)
        main_menu()
        return choice
    if choice ==2:  #adding item
        new_menu(unique_dict,unique_string)
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




def courier_menu():
    #food_dict = af.import_products()
    unique_dict = courier_dict
    unique_string = "courier"
    unique_list = ['Main Menu', f'Print {unique_string.title()} List', f'Create New {unique_string.title()}',
          f'UPDATE Exising {unique_string.title()}', f'DELETE Existing {unique_string.title()}']

    os.system('clear')
    print(f"This is the {unique_string}s menu\n")
    choice = selection_catcher(unique_list,message = "COURIER MENU",include_99=0,art=courier_art)
    if choice == 0: #returning to main menu
        main_menu()
    if choice == 1: #printing items
        os.system('clear')
        print_dict(unique_dict)
        main_menu()
        return choice
    if choice ==2:  #adding item
        new_menu(unique_dict,unique_string)
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
####################################################################################################
####################################################################################################
###     ORDER MENU
####################################################################################################
####################################################################################################
def order_menu():
    os.system('clear')
    print(order_art)
    unique_string = "order"
    print(f"This is the {unique_string}s menu\n")
    unique_list = ['Main Menu', f'Print {unique_string.title()} List', f'Create New {unique_string.title()}',
          f'UPDATE Exising {unique_string.title()}', f'DELETE Existing {unique_string.title()}']
    os.system('clear')
    print(f"This is the {unique_string}s menu\n")
    choice = selection_catcher(unique_list,message = "ORDERS MENU",include_99=0,art=order_art)
    if choice == 0: #returning to main menu
        main_menu()
    if choice == 1: #printing items
        os.system('clear')
        print_list_of_dict(orders_list)
        main_menu()
        return choice
    if choice ==2:  #adding item
        new_order(orders_list,unique_string)
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
###     APPEND MENU - PRODUCT AND COURIER
####################################################################################################
####################################################################################################

def new_menu(unique_dict,category: str = None): #use for products and couriers
    #initialising choice_list
    choice_list = list(unique_dict.keys())
    os.system('clear')
    if category == "courier":
        print(new_courier_art)
    else:
        print(new_product_art)

    choice = selection_catcher(choice_list,
                               message = f"Please select the subset of {category} you would like to add",include_99=1)
    # print(choice)
    # print(choice_list[choice])
    # input("WAIT")
    selection = choice_list[choice]
    print(f"You have selected: {selection}")
    print_dynamic_list(unique_dict[selection])
    new_item = input(f"Please enter the name of the {category} you would like to add\n")
    if new_item =="": #no blank catcher
        print("You cannot add a blank product, please type in a meaningful name for this product")
        print("You will be redirected to select the subset again")
        time.sleep(2)
        new_menu(unique_dict,category)
    else:
        unique_dict[selection].append(new_item)
        os.system('clear')
        #persist the data by writing to txt file
        af.export_product_csv(unique_dict)
        print(f"{category.title()} has been successfully updated")
        print(f"The new {category} list is as below")
        print_dict(unique_dict)
        main_menu()
            # This coding below is to work out which category of item to add




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


    
def update_menu():
    pass

def delete_menu():
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