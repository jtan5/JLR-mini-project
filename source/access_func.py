# this module generally controls the opening and closing of files and the mappings

import os



def import_products():
    
    choice_list = []#['Drinks', 'Cold food', 'Hot food']
    #drinks = []#['Still water 500ml', 'Sparking water 500ml', 'Fanta Zero 350ml',
            #'Coke Zero 350ml', 'Don Perignon in paper bag 350ml']
    #cold_food = []#['Vegan sandwich', 'Chicken sandwich', 'Cheese block']
    #hot_food = []#["Vegan pie", "Meat pie",
                #"Jacket potato with beans", "Fish and chips"]
    category_new = []
    
    current_path = os.getcwd()
    parent_path = os.path.dirname(current_path)
    print("Current Directory: ", current_path)
    print("Parent Directory: ", parent_path)

    products_file = os.path.join(parent_path, "products", "hot_food.txt")
    products_path = os.path.join(parent_path, "products")
    print("Products_file: ", products_file)
    print("Products_path: ", products_path)

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
            #text = file.read()
            #print(text)
            globals()[filename.strip(".txt")] = file.read().splitlines(0)
            # print(f"Initial filename contents: {filename}")
            # for line_index, line_value in enumerate(file.readlines()):
            #     clean_name = line_value.rstrip()
            #     print(f"clean_name: {clean_name}")
            #     filename[line_index] = clean_name
            #     print(f"For line_index {line_index}:{clean_name}")
            print(f"Final filename contents of file: {clean_name}: {globals()[clean_name]}")
            
    
    
    # with open('studentnames.txt', 'r') as file:
    #     for line in file.readlines():
    #         clean_name = line.rstrip()
    #         print(clean_name)
    
import_products()