# this module generally controls the opening and closing of files and the mappings

import os


#module below used to presist data by importing txt files from products folder
def import_products():
    
    global choice_list
    choice_list = []#['Drinks', 'Cold food', 'Hot food']
    ### the below is no longer required as it is controlled as global variables ###
    #drinks = []#['Still water 500ml', 'Sparking water 500ml', 'Fanta Zero 350ml',
            #'Coke Zero 350ml', 'Don Perignon in paper bag 350ml']
    #cold_food = []#['Vegan sandwich', 'Chicken sandwich', 'Cheese block']
    #hot_food = []#["Vegan pie", "Meat pie",
                #"Jacket potato with beans", "Fish and chips"]
    global food_dict
    food_dict = dict()
                
    #sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    #print("Current Directory: ", current_path)
    #print("Parent Directory: ", parent_path)
    products_file = os.path.join(parent_path, "products", "hot_food.txt")
    products_path = os.path.join(parent_path, "products")
    #print("Products_file: ", products_file)
    #print("Products_path: ", products_path)

    for index, filename in enumerate(os.listdir(products_path)):
        print("printing filename",index,filename)
        #starting with an empty list, populating choicelist based on filenames, stripping out .txt
        clean_name = filename.strip(".txt")
        choice_list.append(clean_name)
        globals()[filename.strip(".txt")] = []
        #exec("%s=%d" % (filename,5000))

        print(f"This is the choise list :{choice_list}")
        #category_new[index] = filename.strip(".txt")
        (os.path.join(products_path, filename))
        with open(os.path.join(products_path, filename), 'r') as file:
            globals()[clean_name] = file.read().splitlines(0)
            #print(f"Final filename contents of file: {clean_name}: {globals()[clean_name]}")

            food_dict[clean_name] = globals()[clean_name]
    #print(f"Final filename contents of file: {choice_list[1]}: {globals()[choice_list[1]]}")
    

#module below used to presist data by exporting food_dict into txt files in products folder
def export_products():
    #sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    products_path = os.path.join(parent_path, "products")
    
    #getting the latest choice_list from food_dict
    choice_list = list(food_dict.keys())
    
    for key in food_dict.keys():
        globals()[key]
        filename = key + ".txt"
        with open(os.path.join(products_path, filename), 'w') as file:
            for product_name in food_dict[key]:
                file.write(product_name + '\n')
    
    
    # for index, product_category in enumerate(choice_list): 
    #     #making sure the global list of product is matching food_dict
    #     globals()[product_category]
    #     filename = product_category + ".txt"
    #     #try:
    #     with open(os.path.join(products_path, filename), 'w') as file:
    #         for product in globals()[choice_list[index]]:
    #             file.write(product + '\n')
    #     #except Exception as e:
    #     #    print('An error occurred: ' + str(e))