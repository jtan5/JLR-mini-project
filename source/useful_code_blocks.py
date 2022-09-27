#QUARANTINE AREA!!!
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