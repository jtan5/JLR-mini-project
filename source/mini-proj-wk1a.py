
#defining menu
#
from replit import clear
#initialising global variables
yes_no = ['No','Yes']
choice_list = ['drinks','cold food','hotfood', 'bakery']
drinks= ['Still water 500ml','Sparking water 500ml','Fanta Zero 350ml', 'Coke Zero 350ml','Don Perignon in paper bag 350ml']


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
drink_art = """
      )  (
     (   ) )
      ) ( (
 mrf_______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
"""
beer_art = """
.~~~~.
i====i_
|cccc|_)
|cccc|   
`-==-'
"""
hot_food_art = """

 __       ___,.-------..__        __
//\\ _,-''                `'--._ //\\
\\ ;'                           `: //
 `(                               )'
   :.                           ,;
    `.`--.___           ___.--','
      `.     ``-------''     ,'
         -.               ,-
            `-._______.-'
"""

def printdynamic(a,question,art,add_option=0):
    #initialising newvalue = 0
    newvalue = 0
    clear()
    print(art)
    print(question)
    for index, val in enumerate(a):
        print(f"{index} - {val}")
    if add_option==1:
        print("70 - Update existing item / category")
        print("71 - Delete existing item / category")
        print("77 - Create new item / category")
    print("88 - Take the blue pill and don't follow the white rabbit\n")

    choice2=int(input("Please enter a valid option as listed above\n"))
    if choice2 == 88:
        print("You have selected to quit.")
        exit()
    
    elif choice2==77:
        newvalue = input("Please enter item/ category name\n")
        choice_list.append(newvalue)
        print(f"The new choice list now looks like this {choice_list}\n")
        return choice2, len(a), newvalue
    else:
        return choice2, len(a), newvalue


### PROGRAM STARTS HERE!

print(food_drink_art)
print('Welcome to the Bootcamp Cafe Setup Page\n')

#!! BLOCK STARTS FOR GATEKEEPER LOGIC
question = "Would you like to add a new product?"
#initialising choice_tuple to run the while loop on first call;
choice_tuple =(99,0,0)
#while loop stops any invalid entries passing through further down
while choice_tuple[0] >= choice_tuple[1]:
    choice_tuple = printdynamic(yes_no,question,food_drink_art)
    #for debugging uncomment line below
    # print(f"You have entered {choice_tuple}")
#logic module for yes_no selection
if choice_tuple[0]==0: #0 for no & 1 for yes
    print("You have chosen to exit\n")
    exit()
else:
    #!! BLOCK STARTS FOR GATEKEEPER LOGIC
    question ="What type of product would you like to add?"
    #choice_list = ['Drinks','Cold food','Hot food', 'Bakery']
    #initialising choice_tuple to run the while loop on first call;
    choice_tuple =(99,0,0)
    #while loop stops any invalid entries passing through further down
    while choice_tuple[0] >= choice_tuple[1]:
        choice_tuple = printdynamic(choice_list,question,food_drink_art,1)
        print(f"You have entered {choice_tuple}")
        #Making a break to enter a new product
        if choice_tuple[0]==70:  #70 for update; 71 for delete
           choice_list.append(choice_tuple[2])
           print(f"The new choice list now looks like this {choice_list}\n")
           break
    #logic module for selection
    if choice_tuple[0]==0:
        print("Drinks")
        #drinks selection
    elif choice_tuple[0]==1:
        print("ColdFood")
        #cold food
    elif choice_tuple[0]==2:
        print("Hot food")
        #hot food
    elif choice_tuple[0]==3:
        print("Bakery")
        #bakery
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