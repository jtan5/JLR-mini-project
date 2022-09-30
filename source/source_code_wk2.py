
# defining menu

#from replit import clear
import os
import access_func as af
# pylint: disable=E1101
# initialising global variables
yes_no = ['No', 'Yes']



af.import_products()
af.import_couriers()


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
        print(f"{index} - {val}")
    if add_option == 1:
        print("99 - Return to main menu")

    choice2 = int(input("Please enter a valid option as listed above\n"))
    if (choice2) < len(a):
        selecteditem = a[choice2]
        return choice2, len(a), selecteditem
    else:
        return choice2, len(a), "Invalid selection"

option1 = ['Quit', 'View all products on menu', 'View all couriers']

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
        menu2()
        return choice_tuple  # continue to next segment
    if choice_tuple[0] == 2: #1 for couriers
        menu2c()
        return choice_tuple  # continue to next segment
    else:
        print("You have entered an invalid command, quiting program.\n")

option2 = ['Main Menu', 'Print Product List', 'Create New Product',
           'UPDATE Exising Product', 'DELETE Existing Product', 'Print Courier List']

def menu2():
    question = "Main Menu - Products"
    # initialising choice_tuple to run the while loop on first call;
    choice_tuple = (99, 0, 0)
    # while loop stops any invalid entries passing through further down
    while choice_tuple[0] >= choice_tuple[1]:
        choice_tuple = printdynamic(option2, question, food_drink_art, 0)
        #print(f"You have entered {choice_tuple}")
    # Making a break to enter a new product

    if choice_tuple[0] == 0:
        menu1()  # back to menu1
        # choice_list.append(choice_tuple[2])
    elif choice_tuple[0] == 1:
        # clear() - using replit
        os.system('clear')
        print("\n".join("{}\t{}".format(k, v) for k, v in af.food_dict.items()))
        # choice_list.append(choice_tuple[2])
        #print(f"The new choice list now looks like this {choice_list}\n")
        input("Press any key to clear screen and return to main menu")
        os.system('clear')
        menu2()
    elif choice_tuple[0] == 2:  # do this if selecting to add new product
        print("Creating new products")
        menu3()
        return choice_tuple
    elif choice_tuple[0] == 3:  # do this if selecting to edit a product
        print("Updating existing products")
        menu4()
        return choice_tuple
    elif choice_tuple[0] == 4:  # do this if selecting to remove a product
        print("Deleting existing products")
        menu5()
        return choice_tuple
    # elif choice_tuple[0] == 5:  # do this if selecting to remove a product
    #     #print("Print list of couriers.\n")
    #     os.system('clear')
    #     print("\n".join("{}\t{}".format(k, v) for k, v in af.couriers_dict.items()))
    #     input("Press any key to clear screen and return to main menu")
    #     os.system('clear')
    #     menu1()

option2c = ['Main Menu', 'Print Couriers List', 'Create New Courier',
           'WIP - UPDATE Exising Courier', 'WIP - DELETE Existing Courier']

def menu2c():
    question = "Main Menu - Couriers"
    # initialising choice_tuple to run the while loop on first call;
    choice_tuple = (99, 0, 0)
    # while loop stops any invalid entries passing through further down
    while choice_tuple[0] >= choice_tuple[1]:
        choice_tuple = printdynamic(option2c, question, courier_art, 0)
        #print(f"You have entered {choice_tuple}")
    # Making a break to enter a new product

    if choice_tuple[0] == 0:
        menu1()  # back to menu1
        # choice_list.append(choice_tuple[2])
    elif choice_tuple[0] == 1:
        #print("Print list of couriers.\n")
        os.system('clear')
        print("\n".join("{}\t{}".format(k, v) for k, v in af.couriers_dict.items()))
        input("Press any key to clear screen and return to main menu")
        os.system('clear')
        menu2c()
    elif choice_tuple[0] == 2:  # do this if selecting to add new product
        print("Creating new courier")
        menu3c()
        return choice_tuple
    elif choice_tuple[0] == 3:  # do this if selecting to edit a product
        print("Updating existing courier")
        #menu4c()
        return choice_tuple
    elif choice_tuple[0] == 4:  # do this if selecting to remove a product
        print("Deleting existing courier")
        #menu5c()
        return choice_tuple

def menu3():
    # menu to add new products
    prod_list = [key for key, val in af.food_dict.items()]
    question = "Select the category of item you would like to add"
    # initialising choice_tuple to run the while loop on first call;
    choice_tuple = (99, 0, 0)
    # while loop stops any invalid entries passing through further down
    while choice_tuple[0] >= choice_tuple[1]:
        choice_tuple = printdynamic(prod_list, question, food_drink_art, 1)
        #print(f"You have entered {choice_tuple}")
        # code to handle 99 break clause
        if choice_tuple[0] == 99:
            input("You have decided to cancel and return to main menu\n")
            menu2()
            break
    # This coding below is to work out which category of item to add
    for index, val in enumerate(af.choice_list):
        #print(f"Assessing if choice_tuple is equal to {index} - {val}")
        if choice_tuple[0] == index:
            # print(
            # f"Choice_tuple 0 is {choice_tuple[0]} & choice list index is {index}")
            print(f"The following list is for {af.choice_list[index]}")
            # cycles through all items in a particular key of food_dict
            for index, val in enumerate(af.food_dict[choice_tuple[2]]):
                print(f"{index} - {val}")
            #print("The list of products")
            # print(food_dict[choice_tuple[2]])
            new_prod = input(
                "Please enter the product that you would like to add\n")
            af.food_dict[choice_tuple[2]].append(new_prod)
            os.system('clear')
            print("The new product list is as below")
            for index, val in enumerate(af.food_dict[choice_tuple[2]]):
                print(f"{index} - {val}")
            #persist the data by writing to txt file
            af.export_products()
            input("Press any key to return to main menu")
            menu2()
        else:
            #print("***DEBUG NOTICE***")
            # print(
            #    f"Choice_tuple 0 is {choice_tuple[0]} & choice list index is {index}")
            os.system('clear')
            print("Excellent choice, products were definately lacking in this category.\n")


def menu3c():
    # menu to add new products
    cour_list = [key for key, val in af.couriers_dict.items()]
    question = "Select the category of item you would like to add"
    # initialising choice_tuple to run the while loop on first call;
    choice_tuple = (99, 0, 0)
    # while loop stops any invalid entries passing through further down
    while choice_tuple[0] >= choice_tuple[1]:
        choice_tuple = printdynamic(cour_list, question, courier_art, 1)
        #print(f"You have entered {choice_tuple}")
        # code to handle 99 break clause
        if choice_tuple[0] == 99:
            input("You have decided to cancel and return to main menu\n")
            menu2()
            break
    # This coding below is to work out which category of item to add
    for index, val in enumerate(af.couriers_list):
        #print(f"Assessing if choice_tuple is equal to {index} - {val}")
        if choice_tuple[0] == index:
            # print(
            # f"Choice_tuple 0 is {choice_tuple[0]} & choice list index is {index}")
            print(f"The following list is for {af.couriers_list[index]}")
            # cycles through all items in a particular key of couriers_dict
            for index, val in enumerate(af.couriers_dict[choice_tuple[2]]):
                print(f"{index} - {val}")
            #print("The list of products")
            # print(couriers_dict[choice_tuple[2]])
            new_courier = input(
                "Please enter the product that you would like to add\n")
            af.couriers_dict[choice_tuple[2]].append(new_courier)
            os.system('clear')
            print("The new courier list is as below")
            for index, val in enumerate(af.couriers_dict[choice_tuple[2]]):
                print(f"{index} - {val}")
            #persist the data by writing to txt file
            af.export_couriers()
            input("Press any key to return to main menu")
            menu2()
        else:
            #print("***DEBUG NOTICE***")
            # print(
            #    f"Choice_tuple 0 is {choice_tuple[0]} & choice list index is {index}")
            os.system('clear')
            print("Excellent choice, products were definately lacking in this category.\n")


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
            menu2()
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
                    menu2()
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


# PROGRAM STARTS HERE!
try:
    menu1()
except ValueError:
    os.system('clear')
    print("Input error, please enter only integers")
except Exception as e:
    os.system('clear')
    print('An error occurred: ' + str(e))