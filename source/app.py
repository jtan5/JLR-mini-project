import os


current_path = os.getcwd()
parent_path = os.path.dirname(current_path)
print("Current Directory: ", current_path)
print("Parent Directory: ", parent_path)

products_file = os.path.join(parent_path, "products", "hot_food.txt")
products_path = os.path.join(parent_path, "products")
print("Products_file: ", products_file)
print("Products_path: ", products_path)
       
        
for filename in os.listdir(products_path):
    print(os.path.join(products_path, filename))
    with open(os.path.join(products_path, filename), 'r') as f:
       text = f.read()
       print(text)