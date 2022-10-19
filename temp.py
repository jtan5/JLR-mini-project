####################################################################################################
####################################################################################################
###     CUSTOMER MENU
####################################################################################################
####################################################################################################
def customer_menu():

    unique_list_of_dict = af.import_customer_db() 
    category = "customer"
    unique_list = ['Main Menu', f'Print {category.title()} List', f'Create New {category.title()}',
          f'UPDATE Exising {category.title()}', f'DELETE Existing {category.title()}']

    os.system('clear')
    print(f"This is the {category}s menu\n")
    choice = selection_catcher(unique_list,message = "customer MENU",art=customer_art)
    if choice == 0: #returning to main menu
        return main_menu()
    if choice == 1: #printing items
        os.system('clear')
        print_list_of_dict(unique_list_of_dict)
        input("Press any key to go back\n")
        return customer_menu()

    if choice ==2:  #adding item
        add_item = new_item(unique_list_of_dict,category)
        if add_item is True:
            print(f"{category.title()} has been added successfully")
        else:
            print(f"Whoops... unable to add new {category}, please check database connection and try again")
        input("Press any key to go back\n")
        return customer_menu()
        

    if choice ==3:  #editing item
        update_item=update_many_items(unique_list_of_dict, category)
        if update_item is True:
            print(f"{category.title()} has been added successfully")
        else:
            print(f"Whoops... unable to add new {category}, please check database connection and try again")
        input("Press any key to go back\n")
        return customer_menu()

    if choice ==4:  #deleting item
        delete_item = delete_item(unique_list_of_dict,category)
        if delete_item is True:
            print(f"{category.title()} has been added successfully")
        else:
            print(f"Whoops... unable to add new {category}, please check database connection and try again")
        input("Press any key to go back\n")
        return customer_menu()