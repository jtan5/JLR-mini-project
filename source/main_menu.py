
# defining menu
import time

import sys
import os
from pathlib import Path
from datetime import datetime
 

os.path.abspath(__file__)
current_path = os.getcwd()
print(current_path)
sys.path.append(os.path.dirname(__file__))
print(sys.path)
import access_func as af
# pylint: disable=E1101
# initialising global variables
yes_no = ['No', 'Yes']



food_dict = af.import_products()        #function returns food_dict
couriers_dict = af.import_couriers()    #function returns couriers dict
orders_list = af.import_orders()        #function returns orders_list


# Decision tree for questions
welcome = "Welcome to the Bootcamp Cafe Setup Page\n"
question = "Would you like to add a new product?"
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

def printdynamic(a, question, art, add_option=0):
    # clear() - using replit
    os.system('clear')
    print(art)
    print(question)
    for index, val in enumerate(a):
        print(f"[{index}] - {val}")
    if add_option == 1:
        print("99 - Return to main menu")

    choice2 = int(input("Please enter a valid option as listed above\n"))
    if (choice2) < len(a):
        selecteditem = a[choice2]
        return choice2, len(a), selecteditem
    else:
        return choice2, len(a), "Invalid selection"


option1 = ['Quit', 'View all products', 'View all couriers','View all orders']

def menu1():
    # initialising choice_tuple to run the while loop on first call;
    choice_tuple = (99, 0, 0)
    # while loop stops any invalid entries passing through further down
    while choice_tuple[0] >= choice_tuple[1] or choice_tuple[0] == None:
        choice_tuple = printdynamic(option1, welcome, food_drink_art)
    # logic module for yes_no selection
    if choice_tuple[0] == 0:  # 0 for quit
        print("You have chosen to exit\n")
        exit()
    if choice_tuple[0] == 1: #1 for products
        menu_type_p = "product"
        question_p = f"Main Menu - {menu_type_p.title()}s"
        option_p = ['Main Menu', 'Print Product List', 'Create New Product',
          'UPDATE Exising Product', 'DELETE Existing Product']
        menu2(question_p,food_dict,option_p,menu_type_p,food_drink_art,af.export_products)
        return choice_tuple  # continue to next segment
    if choice_tuple[0] == 2: #2 for couriers
        menu_type_c = "courier"
        question_c = f"Main Menu - {menu_type_c.title()}s"
        option_2c = ['Main Menu', 'Print Couriers List', 'Create New Courier',
           'WIP - UPDATE Exising Courier', 'WIP - DELETE Existing Courier']
        art = courier_art
        menu2(question_c,couriers_dict,option_2c,menu_type_c,courier_art,af.export_couriers)
        return choice_tuple  # continue to next segment
    if choice_tuple[0] == 3: #3 for orders
        menu_type_o = "order"
        question_o = f"Main Menu - {menu_type_o.title()}s"
        option_o = ['Main Menu', 'Print Orders List', 'Create New Order',
           'WIP - UPDATE Exising Order', 'WIP - DELETE Existing Order']
        art = courier_art
        menu2(question_o,af.dummy_dict,option_o,menu_type_o,courier_art,af.export_orders)
        return choice_tuple  # continue to next segment
    else:
        print("You have entered an invalid command, quiting program.\n")

option_D = ['Main Menu', '<DEFAULT LIST-CHECK YOUR CODE>'] #Debugging line

def menu2(question:str=question, func_dict:dict=af.dummy_dict, option_list:list=option_D,menu_type:str="<PROD_TYPE>",art=food_drink_art,func_export=af.export_products):
    # initialising choice_tuple to run the while loop on first call;
    choice_tuple = (99, 0, 0)
    # while loop stops any invalid entries passing through further down
    while choice_tuple[0] >= choice_tuple[1]:
        choice_tuple = printdynamic(option_list, question, food_drink_art, 0)
        #print(f"You have entered {choice_tuple}")
    # Making a break to enter a new product
    
    if choice_tuple[0] == 0:
        menu1()  # back to menu1
        # choice_list.append(choice_tuple[2])
    elif choice_tuple[0] == 1:
        os.system('clear')
        if menu_type == "order": #order is maintained in a master list as opposed to a dict
            for i, _ in enumerate(orders_list):
                print(f"This is order {i+1} of {len(orders_list)}")
                print("\n".join(f"{k:<25}{v}" for k, v in orders_list[i].items()))
                if i+1 ==len(orders_list):
                    print("This is the last record")
                else:
                    input("Press any key to see next order")
            input("Press any key to clear screen and return to main menu")
            os.system('clear')
            menu1()
        else: #to cater for products and couriers
            print("\n".join(f"{k:<20}{v}\n" for k, v in func_dict.items()))
            input("Press any key to clear screen and return to main menu")
            os.system('clear')
            menu1()
    elif choice_tuple[0] == 2:  # do this if selecting to add new product

        #Initialising variables for menu3 - start
        question = f"Select the subset of {menu_type}s you would like to add"
        #Initialising variables for menu3 - end
        print(f"Creating new {menu_type}s")
        menu3(question,func_dict,menu_type,food_drink_art,func_export)
        return choice_tuple
    elif choice_tuple[0] == 3:  # do this if selecting to edit a product
        print(f"Updating existing {menu_type}s")
        menu4()
        return choice_tuple
    elif choice_tuple[0] == 4:  # do this if selecting to remove a product
        print(f"Deleting existing {menu_type}s")
        menu5()
        return choice_tuple


def menu3(question:str=question, # menu to add new products, couriers or orders
          func_dict:dict=af.dummy_dict, 
          menu_type:str="product",
          art=food_drink_art,
          func_export=af.export_products): 

    #included if block to cater for order
    if menu_type == "order":
        new_order = {}
        new_order["customer_name"] = input("Please enter customer name\n")
        new_order["customer_address_1"] = input("Please enter first line address\n")
        new_order["customer_address_2"] = input("Please enter second line address\nEg: London, Amsterdam, Bogota\n")
        new_order["customer_postcode"] = input("Please enter customer postcode\n")
        new_order["courier_no"] = int(input("Please enter courier number\n"))
        dt_obj = datetime.now()
        new_order["order_time"] = f'ordertaken_{dt_obj: %Y%m%d_%H%M}', #'creating timestamp
        new_order["status"] = "new"
        
        #saving the new_order into orders_list
        orders_list.append(new_order)
        af.export_orders(orders_list)
        
    else:
        prod_list = [key for key, val in func_dict.items()]
        choice_list = list(func_dict.keys())
        # initialising choice_tuple to run the while loop on first call;
        choice_tuple = (99, 0, 0)

        # while loop stops any invalid entries passing through further down
        while choice_tuple[0] >= choice_tuple[1]:
            choice_tuple = printdynamic(prod_list, question, art, 1)
            #print(f"You have entered {choice_tuple}")
            # code to handle 99 break clause
            if choice_tuple[0] == 99:
                menu1()
                break
        # This coding below is to work out which category of item to add
        for index, val in enumerate(choice_list):
            if choice_tuple[0] == index:
                # print(
                # f"Choice_tuple 0 is {choice_tuple[0]} & choice list index is {index}")
                print(f"The following list is for {choice_list[index]}")
                # cycles through all items in a particular key of food_dict
                for index, val in enumerate(func_dict[choice_tuple[2]]):
                    print(f"{index} - {val}")
                #print("The list of products")
                # print(food_dict[choice_tuple[2]])
                new_prod = input(
                    f"Please enter the {menu_type} that you would like to add\n")
                func_dict[choice_tuple[2]].append(new_prod)
                os.system('clear')
                print(f"The new {menu_type} list is as below")
                for index, val in enumerate(func_dict[choice_tuple[2]]):
                    print(f"{index} - {val}")
                #persist the data by writing to txt file
                func_export()
                menu1()
            else:
                #print("***DEBUG NOTICE***")
                # print(
                #    f"Choice_tuple 0 is {choice_tuple[0]} & choice list index is {index}")
                os.system('clear')
                print(f"Excellent choice, {menu_type}s were definately lacking in this category.\n")



def menu4():
    # menu to append existing products
    # prod_list is the keys of food_dict
    prod_list = [key for key, val in af.food_dict.items()]
    question = "Select the category of item you would like to edit"
    # initialising choice_tuple to run the while loop on first call;
    choice_tuple = (99, 0, 0)
    # while loop stops any invalid entries passing through further down
    while choice_tuple[0] >= choice_tuple[1]:
        choice_tuple = printdynamic(prod_list, question, food_drink_art, 1)
        #print(f"You have entered {choice_tuple}")
        # code to handle 99 break clause
        if choice_tuple[0] == 99:
            input("You have decided to cancel and return to main menu\n")
            question = "Main Menu - Products"
            option2 = ['Main Menu', 'Print Product List', 'Create New Product',
            'UPDATE Exising Product', 'DELETE Existing Product', 'Print Courier List']
            menu_type = "product"
            menu2(question,af.food_dict,option2,menu_type)
            break
    # saving the results from choice_tuple (mainly category name/ index) for later reference
    # IMPORTANT!!!
    desired_cat = choice_tuple
    # This coding below is to work out which category of item to add
    for index, val in enumerate(af.choice_list):  # drinks, hot_food, cold food
        #print(f"Assessing if choice_tuple is equal to {index} - {val}")
        if choice_tuple[0] == index:
            # debug line
            # print(
            #    f"Choice_tuple 0 is {choice_tuple[0]} & choice list index is {index}")
            # debug line
            #print(f"The following list is for {choice_list[index]}")
            # cycles through all items in a particular key of food_dict
            for index, val in enumerate(af.food_dict[choice_tuple[2]]):
                print(f"{index} - {val}")
            print(f"The list of products {af.food_dict[choice_tuple[2]]}")
            edit_list = af.food_dict[choice_tuple[2]]
            question = "Select the item you would like to edit"
            choice_tuple = (99, 0, 0)
            # while loop stops any invalid entries passing through further down
            while choice_tuple[0] >= choice_tuple[1]:
                choice_tuple = printdynamic(
                    edit_list, question, food_drink_art, 1)

                # code to handle 99 break clause
                if choice_tuple[0] == 99:
                    input("You have decided to cancel and return to main menu\n")
                    menu2(question,af.food_dict,option2,menu_type)
                    break
            # saving the category selection into a meaningful name

            # for index, val in enumerate(edit_list): #this loop is to iterate through the hot_food items eg: [Vegan pie, meat pie, etc]
                # if choice_tuple[0] == index:
            #print(f"You have entered {choice_tuple}")
            # notreq print(f"Assessing if choice_tuple is equal to {index} - {val}")
            #print(f"Previously you have entered {desired_cat}")
            #print(f"food_dict[desired_cat[2]] {food_dict[desired_cat[2]]}")
            #print(f"the name of selection from food dict {food_dict[desired_cat[2]][choice_tuple[0]]}")
            new_prod_name = input(
                f"Instead of {af.food_dict[desired_cat[2]][choice_tuple[0]]} \nWhat would you like this product to be called instead?\n")
            af.food_dict[desired_cat[2]][choice_tuple[0]] = new_prod_name
            #edit_list[index] = new_prod_name
            # food_dict[choice_tuple[2]]
            # food_dict[choice_tuple[2]].append(new_prod)
            os.system('clear')
            print("The new product list is as below")
            for index, val in enumerate(af.food_dict[desired_cat[2]]):
                print(f"{index} - {val}")
            #persist the data by writing to txt file
            af.export_products()
            input("Press any key to return to main menu")
            menu2()
        else:
            # print(
            #    f"Choice_tuple 0 is {choice_tuple[0]} & choice list index is {index}")
            #print("it does not match")
            os.system('clear')


def menu5():
    # menu to delete existing products
    # prod_list is the keys of food_dict
    prod_list = [key for key, val in af.food_dict.items()]
    question = "What category is the item you would like to delete in?"
    # initialising choice_tuple to run the while loop on first call;
    choice_tuple = (99, 0, 0)
    # while loop stops any invalid entries passing through further down
    while choice_tuple[0] >= choice_tuple[1]:
        choice_tuple = printdynamic(prod_list, question, food_drink_art, 0)
        #print(f"You have entered {choice_tuple}")
        # code to handle 99 break clause
        if choice_tuple[0] == 99:
            input("You have decided to cancel and return to main menu\n")
            menu2()
            break
    # saving the results from choice_tuple (mainly category name/ index) for later reference
    # IMPORTANT!!!
    desired_cat = choice_tuple
    # This coding below is to work out which category of item to add
    for index, val in enumerate(af.choice_list):  # drinks, hot_food, cold food
        #print(f"Assessing if choice_tuple is equal to {index} - {val}")
        if choice_tuple[0] == index:
            # print(f"Choice_tuple 0 is {choice_tuple[0]} & choice list index is {index}")   #debug line
            # print(f"The following list is for {choice_list[index]}")                       #debug line
            # cycles through all items in a particular key of food_dict
            for index, val in enumerate(af.food_dict[choice_tuple[2]]):
                print(f"{index} - {val}")
            print(f"The list of products {af.food_dict[choice_tuple[2]]}")
            edit_list = af.food_dict[choice_tuple[2]]
            question = "Select the item you would like to delete"
            choice_tuple = (99, 0, 0)
            # while loop stops any invalid entries passing through further down
            while choice_tuple[0] >= choice_tuple[1]:
                choice_tuple = printdynamic(
                    edit_list, question, food_drink_art, 1)

                # code to handle 99 break clause
                if choice_tuple[0] == 99:
                    input("You have decided to cancel and return to main menu\n")
                    menu2()
                    break
            # saving the category selection into a meaningful name

            # copy is a shallow copy. it only copies 1 level.!!
            edit_list_new = edit_list.copy()
            edit_list_new.remove(choice_tuple[2])
            af.food_dict[desired_cat[2]] = edit_list_new

            os.system('clear')
            print("The new product list is as below")
            for index, val in enumerate(af.food_dict[desired_cat[2]]):
                print(f"{index} - {val}")
            input("Press any key to return to main menu")
            af.export_products()
            menu2()
        else:
            print(
                f"Choice_tuple 0 is {choice_tuple[0]} & choice list index is {index}")
            print("it does not match")


# # PROGRAM STARTS HERE!
# try:
#     menu1()
# except ValueError:
#     os.system('clear')
#     print("Input error, please enter only integers")
# except Exception as e:
#     os.system('clear')
#     print('An error occurred: ' + str(e))