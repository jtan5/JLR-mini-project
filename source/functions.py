import os
import sys
import time
import random
import tabulate
from pathlib import Path
from datetime import datetime
from traceback import print_list
from unicodedata import category
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from .art import area_art


####################################################################################################
####################################################################################################
###     SELECTION CATCHER
####################################################################################################
####################################################################################################
def selection_catcher(func_list: list,message: str,art=None):
    choice = 50
    while choice >=len(func_list):
        #os.system("clear")
        print(art)
        print(message)
        print_dynamic_list(func_list)
        try: 
            choice = int(input("Please enter a valid option as listed above\n"))
        except ValueError:
            os.system('clear')
            print('You have entered a non-numerical / blank value\n\n\n')
            print("Menu will load shortly...")
            time.sleep(2)
            return selection_catcher(func_list,message,art)
    return choice
    
    
####################################################################################################
####################################################################################################
###     SELECTION CATCHER DICT
####################################################################################################
####################################################################################################
def selection_catcher_dict(func_list: list,message: str,art=None):
    choice = 50
    while choice >=len(func_list):
        #os.system("clear")
        print(art)
        print(message)
        print_list_of_dict_selection(func_list)
        try: 
            choice = int(input("Please enter a valid option as listed above\n"))
            #print(choice)
        except ValueError:
            os.system('clear')
            print('You have entered a non-numerical / blank value\n\n\n')
            print("Menu will load shortly...")
            time.sleep(2)
            return selection_catcher_dict(func_list,message,art)
    return choice
####################################################################################################
###     PRINT DYNAMIC LIST
####################################################################################################
def print_dynamic_list(selection_list):
    if selection_list is None:
        selection_list = ["DEBUG LIST", "LIST_ID1","LIST_ID2"]
    for index, val in enumerate(selection_list):
        print(f"[{index}] - {val}")
###################################################################################################
##     PRINT DICT
###################################################################################################
def print_dict(func_dict):
    print("\t".join(f"{k:>10}:{v:<20}" for k, v in func_dict.items()))
    return func_dict

####################################################################################################
###     PRINT LIST OF DICT - FOR INFO ONLY, NO INDEX
####################################################################################################
def print_list_of_dict(func_list):
    """
    This function prints the dictionaries formatted in tabular form 
    using the Python library tabulate
    """
    header = func_list[0].keys()
    rows =  [dict_item.values() for dict_item in func_list]
    print(tabulate.tabulate(rows, header))
    return func_list
####################################################################################################
###     PRINT LIST OF DICT - FOR SELECTION <INCLUDES INDEX>
####################################################################################################
def print_list_of_dict_selection(func_list):
    for i,_ in enumerate(func_list): 
        data = ""
        key_num = 0
        
        for key,value in func_list[i].items():
            data = data + f"{key:>15}:{value:<20}"
            if key_num == len(func_list[i])-1: #only for the last key/value pair print out
                printobj = f"[{i:>2}] -> {data}".replace("{","").replace("}", "").replace("'","")
                print(printobj)
            key_num +=1
    return func_list

    
####################################################################################################
####################################################################################################
###     BLANK CATCHER
####################################################################################################
####################################################################################################
def blank_catcher(message: str,allow_blanks = False):
    if allow_blanks == False:
        new_item = ""
        while new_item == "" or new_item == 0: #no blank catcher
            new_item = input(f"{message}\n")
    else:
        new_item = input(f"{message}\n")
    return new_item

####################################################################################################
####################################################################################################
###     PRICE CATCHER
####################################################################################################
####################################################################################################
def price_catcher(message: str,allow_blanks = False):
    new_item = ""
    if allow_blanks == False:
        while new_item == "" or new_item == 0: #no blank catchertry: 
            try:
                new_item = round(float(input(f"{message}\n")),2)
            except ValueError:
                os.system('clear')
                print('You have entered a non-numerical / blank value\n\n\n')
                print("Menu will load shortly...")
                time.sleep(2)
                return price_catcher(message,allow_blanks)
    return new_item

####################################################################################################
####################################################################################################
###     INT CATCHER
####################################################################################################
####################################################################################################
def int_catcher(message: str):
    new_item = ""
    while new_item == "" or new_item == 0: #no blank catchertry: 
        try:
            new_item = int(input(f"{message}\n"))
        except ValueError:
            os.system('clear')
            print('You have entered a non-numerical / blank value\n\n\n')
            print("Menu will load shortly...")
            time.sleep(2)
            return int_catcher(message)
    return new_item
####################################################################################################
####################################################################################################
###     PHONE CATCHER
####################################################################################################
####################################################################################################
def phone_catcher():
    try:
        #number = "+447123456789"
        number = input("Please enter courier mobile phone number by beginning with the country code\neg: +447123456789\n")
        mobile_number = carrier._is_mobile(number_type(phonenumbers.parse(number)))
        if mobile_number is True:
            number = number.replace(" ","")
            return number
        else:
            print(f"The phone number you have entered is not a valid mobile number, please re-enter\nEntry screen will reload shortly...\n")
            time.sleep(2)
            return phone_catcher()
    except Exception as e:
        print(f"Error with phone number, error code: {e}\n")
        #print(f"exception start here {number}")
        time.sleep(2)
        return phone_catcher()
        

####################################################################################################
####################################################################################################
###     SERVICING AREA CATCHER
####################################################################################################
####################################################################################################
def servicing_area_catcher():
    areas = ["Greater London", "West Midlands", "District-9", "Area-51"]
    message = "Please enter servicing area"
    choice = selection_catcher(areas,message,area_art)
    return areas[choice]

####################################################################################################
###     YES NO CATCHER
####################################################################################################
def yes_no_catcher(question,art=None):
    yes_no = ["No","Yes"]
    return yes_no[selection_catcher(yes_no,question,art)]