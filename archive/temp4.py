import os

os.system('clear')
print("food_drink_art")
print("Welcome to the Bootcamp Cafe Setup Page\n")
main_menu_list = ['Quit', 'View all products', 'View all couriers','View all orders']
#print_dynamic_list(main_menu_list)
choice = int(input("Please enter a valid option as listed above\n"))
print(choice.isdigit())