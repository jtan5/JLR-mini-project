
#defining menu
#
from replit import clear
#initialising global variables
yes_no = ['Yes','No']
choice_list = ['Drinks','Cold food','Hot food', 'Bakery', 'Confectionary','Section-9']
drink_list = ['Still water 500ml','Sparking water 500ml','Fanta Zero 350ml', 'Coke Zero 350ml','Don Perignon in paper bag 350ml']


#Decision tree for questions
add_product = "Would you like to add a new product?"

#Images
food_drink_art ='''
  ;)( ;
 :----:     o8Oo./
C|====| ._o8o8o8Oo_.
 |    |  \========/
 `----'   `------'
 '''

# def entrytype0():
#     choice1 = int(input('''
#     Please enter correct category of product you wish to add.
#     1 - Drinks
#     2 - Cold food
#     3 - Hot food
#     4 - Bakery
#     5 - Confectionery
    
#     '''))
#     return choice1

def printdynamic(a,question,art):
    clear()
    print(art)
    print(question)
    for index, val in enumerate(a):
        print(f"{index} - {val}")
    print("88 - Take the blue pill and don't follow the white rabbit\n")
    choice2=int(input("Please enter a valid option as listed above\n"))
    if choice2 == 88:
        print("You have selected to quit.")
        exit()
    else:
        return choice2, len(a)

    # 1 - Drinks
    # 2 - Cold food
    # 3 - Hot food
    # 4 - Bakery
    # 5 - Confectionery


### PROGRAM STARTS HERE!

print(food_drink_art)
print('Welcome to the Bootcamp Cafe Setup Page\n')

#!! BLOCK STARTS FOR GATEKEEPER LOGIC
#initialising choice_tuple to run the while loop on first call;
choice_tuple =(99,0)
#while loop stops any invalid entries passing through further down
while choice_tuple[0] >= choice_tuple[1]:
    choice_tuple = printdynamic(yes_no,add_product,food_drink_art)
    print(f"You have entered {choice_tuple}")
#logic module for yes_no selection
print('This will now step forward to the next part')
#!! BLOCK ENDS FOR GATEKEEPER LOGIC













# a1 = entrytype0(yes_no)
# for yes_no list, 1 is for quiting
# if a1 == "1":
    # quit()
# else:
    # print("Keep going")
    # entrytype0(choice_list)
    #define program for menu
    

# CREATE products listn
# PRINT main menu options
# GET user input for main menu option
# IF user input is 0:
# EXIT app
# products menu
# ELSE IF user input is 1:
# PRINT product menu options
# GET user input for product menu option
# IF user input is 0:
# RETURN to main menu
# ELSE IF user input is 1:
# PRINT products list
# ELSE IF user input is 2:
# CREATE new product
# GET user input for product name
# APPEND product name to products list
# ELSE IF user input is 3:
# STRETCH GOAL - UPDATE existing product
# PRINT product names with its index value
# GET user input for product index value
# GET user input for new product name
# UPDATE product name at index in products list
# ELSE IF user input is 4:
# STRETCH GOAL - DELETE product
# PRINT products list
# GET user input for product index value
# DELETE product at index in products list