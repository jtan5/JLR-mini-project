# this module generally controls the opening and closing of files and the mappings

import os


#module below used to presist data by importing txt files from products folder
def import_products():
    
    global choice_list
    choice_list = []#['Drinks', 'Cold food', 'Hot food']

    global food_dict
    food_dict = dict()
                
    #sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    #print("Current Directory: ", current_path)
    #print("Parent Directory: ", parent_path)
    #products_file = os.path.join(parent_path, "products", "hot_food.txt")
    products_path = os.path.join(parent_path, "products")
    #print("Products_file: ", products_file)
    #print("Products_path: ", products_path)

    for index, filename in enumerate(os.listdir(products_path)):
        print("printing filename",index,filename)
        #starting with an empty list, populating choicelist based on filenames, stripping out .txt
        clean_name = filename.strip(".txt")
        choice_list.append(clean_name)
        globals()[filename.strip(".txt")] = []
        

        #print(f"This is the choise list :{choice_list}")
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
 
            
def import_couriers():
    global couriers_list
    couriers_list = []
    
    global couriers_dict
    couriers_dict = {}
    # global choice_list
    # choice_list = []#['Drinks', 'Cold food', 'Hot food']

    # global food_dict
    # food_dict = dict()
                
    #sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    #print("Current Directory: ", current_path)
    #print("Parent Directory: ", parent_path)
    #products_file = os.path.join(parent_path, "products", "hot_food.txt")
    #products_path = os.path.join(parent_path, "products")
    couriers_path = os.path.join(parent_path, "couriers")
    #print("Products_file: ", products_file)
    #print("Products_path: ", products_path)

    for index, filename in enumerate(os.listdir(couriers_path)):
        print("printing filename with index ",index,filename)
        #starting with an empty list, populating choicelist based on filenames, stripping out .txt
        clean_name = filename.strip(".txt")
        couriers_list.append(clean_name)
        globals()[filename.strip(".txt")] = []
        

        #print(f"This is the choise list :{choice_list}")
        #category_new[index] = filename.strip(".txt")
        (os.path.join(couriers_path, filename))
        with open(os.path.join(couriers_path, filename), 'r') as file:
            globals()[clean_name] = file.read().splitlines(0)
            #print(f"Final filename contents of file: {clean_name}: {globals()[clean_name]}")
            couriers_dict[clean_name] = globals()[clean_name]
    print(f"Final filename contents of file: {couriers_list[-1]}: {globals()[couriers_list[-1]]}")
    
def export_couriers():
    #sorting out the correct directories
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    couriers_path = os.path.join(parent_path, "couriers")
    
    #getting the latest choice_list from food_dict
    courier_list = list(couriers_dict.keys())
    
    for key in couriers_dict.keys():
        globals()[key]
        filename = key + ".txt"
        with open(os.path.join(couriers_path, filename), 'w') as file:
            for product_name in couriers_dict[key]:
                file.write(product_name + '\n')
 