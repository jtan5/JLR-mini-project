def menu3c():
    # menu to add new products
    cour_list = [key for key, val in af.couriers_dict.items()]
    question = "Select the category of item you would like to add"
    # initialising choice_tuple to run the while loop on first call;
    choice_tuple = (99, 0, 0)
    # while loop stops any invalid entries passing through further down
    while choice_tuple[0] >= choice_tuple[1]:
        choice_tuple = printdynamic(cour_list, question, food_drink_art, 1)
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
            print("The new product list is as below")
            for index, val in enumerate(af.couriers_dict[choice_tuple[2]]):
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

