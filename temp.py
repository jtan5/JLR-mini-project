# from source.menu import boolean_catcher, int_catcher,blank_catcher, print_list_of_dict, selection_catcher,selection_catcher_dict,print_list_of_dict_selection, area_art, customer_art, order_art, food_drink_art
# #from source.db_functions import return_invoice_list,get_customer_servicing_area, get_new_customer_id, insert_customer, get_matching_courier, insert_order, insert_order_products, read_from_db, return_invoice_total,update_stock
# from source import access_func as af
# import time
# import os
# import itertools
# import random


# ####################################################################################################
# ###     GET CUSTOMER ID
# ####################################################################################################
# def get_customer_id():
#     question = "Is this customer first order?"
#     yes_no = ["Yes","No"]
#     new_customer_response = yes_no[selection_catcher(yes_no,question,0,customer_art)]
    
#     if new_customer_response == "Yes":
#         new_customer_order = True
#         customer_id = new_customer_entry()
#         #print(f"customer id: {customer_id}")
#     else: #not the customer's first order
#         new_customer_order = False
#         customer_list = af.import_customer_db()
#         #print_list_of_dict_selection(customer_list)
#         #question = "Please select customer from database"
#         customer_id = customer_list[selection_catcher_dict(customer_list,question,0,customer_art)]['customer_id']
#         #print("customer_id:", customer_id)
#     return customer_id

# ####################################################################################################
# ###     NEW CUSTOMER ENTRY
# ####################################################################################################
# def new_customer_entry():
#     question = "Please enter customer name"
#     name = blank_catcher(question)
#     question = "Please enter customer address"
#     address = blank_catcher(question)
#     question = "Please enter customer postcode"
#     postcode = blank_catcher(question)
#     areas = ["Greater London", "West Midlands", "District-9", "Area-51"]
#     question = "Please enter courier servicing area"
#     servicing_area = areas[selection_catcher(areas,question,0,area_art)]
#     #instead of returning here; consider adding db link directly to save to new customer db
#     af.insert_customer(name, address, postcode, servicing_area)
#     customer_id = af.get_new_customer_id(name, address)
#     return customer_id
        


# ####################################################################################################
# ###    GET COURIER ID
# ####################################################################################################
# def get_courier_id(customer_servicing_area: str):
#     available_courier_list = af.get_matching_courier(customer_servicing_area)
#     #get length of list to use randint function
#     # print(available_courier_list)
#     # print(len(available_courier_list))
#     lucky_index = random.randint(0,len(available_courier_list)-1)
#     #selected courier
#     lucky_courier_id = available_courier_list[lucky_index]["courier_id"]
#     #print("selected courier id:", lucky_courier_id)
#     return lucky_courier_id
    
# #get_courier_id("West Midlands")


# ####################################################################################################
# ###    GET ORDER ID
# ####################################################################################################
# def get_order_id(order_dict: dict):
#     #creating temp description for order
#     order_dict["temp_description"] = random.randint(-2147483648,2147483647)
    
#     order_id = af.insert_order(order_dict)
#     print("order_id:", order_id)
#     return order_id
    

# # test_dict = {"courier_id": 4, "customer_id": 5, "order_status" : "New"}
# # test_order_id = get_order_id(test_dict)
# # print(test_order_id)


# ####################################################################################################
# ###    GET ORDER PRODUCTS
# ####################################################################################################
# def get_order_products(order_id: int, customer_id: int, courier_id: int):
    
#     #create op_dict - this is to track all products to attach to this order
#     op_list = []
    
    
#     product_list = af.import_product_db()
#     product_add = 1#counter to keep looping to add products
#     while product_add == 1:
#         #select product to add to order
#         op_dict = {"order_id": order_id, "customer_id": customer_id,"courier_id" : courier_id}
        
#         os.system('clear')
#         #print_list_of_dict_selection(product_list) #displaying product list for selection
#         question = "Please select a product to add to this order"
#         prod_choice = selection_catcher_dict(product_list,question,0,food_drink_art)
#         quantity_question = f"Please enter the quantity of {product_list[prod_choice]['product_name']} you would like to order"
#         q_choice = int_catcher(quantity_question)
#         #logic to compare the quantity vs stock
#         while q_choice > product_list[prod_choice]['stock']: #unhappy path
#             print(f"Unable to select product, there is only {product_list[prod_choice]['stock']} units available for this order")
#             quantity_question = f"Please enter the quantity of {product_list[prod_choice]['product_name']} you would like to order"
#             q_choice = int_catcher(quantity_question)
#         #append details of product and quantity to order
#         op_dict["product_id"] = product_list[prod_choice]["product_id"]
#         op_dict["product_quantity"] = q_choice
#         op_dict["product_name"] = product_list[prod_choice]["product_name"] #for info only - not uploaded to database
#         op_list.append(op_dict)
#         #drop the product_id from the product_list
#         dropped_product = product_list.pop(prod_choice)
#         print("dropped product:", dropped_product)
#         print("op_dict", op_dict)
#         print("op_list", op_list)
#         #asking to add another product
#         no_yes = ["No","Yes"]
#         question_3 = "Would you like to add another product to this order?"
#         product_add = selection_catcher(no_yes,question_3,0,food_drink_art)
#     return op_list
        
        
# # order7_product_list = get_order_products(7)
# # print(order7_product_list)


# ####################################################################################################
# ###    CREATE ORDER INVOICE
# ####################################################################################################
# def create_order_invoice(order_id:int):
#     #run query to get print list
#     invoice_list = af.return_invoice_list(order_id)
#     order_status = invoice_list[0]["order_status"]
#     customer_name = invoice_list[0]["customer_name"]
#     courier_name = invoice_list[0]["courier_name"]
#     print("***********************************************")
#     print(f"Order ID: {order_id}")
#     print(f"Order Status: {order_status}")
#     print(f"Customer Name: {customer_name}")
#     print(f"Courier Name: {courier_name}")
#     print("***********************************************")
#     for i,_ in enumerate(invoice_list):
#         invoice_list[i].pop("order_id")
#         invoice_list[i].pop("order_status")
#         invoice_list[i].pop("customer_name")
#         invoice_list[i].pop("courier_name")
#     print_list_of_dict_selection(invoice_list)
#     invoice_total = af.return_invoice_total(order_id)
#     print("***********************************************")
#     print(f"Total amount due: £{invoice_total:.2f}")
#     print("***********************************************")

# ####################################################################################################
# ####################################################################################################
# ###    CREATE NEW ORDER
# ####################################################################################################
# ####################################################################################################
# def create_new_order():
#     #get customer id
#     customer_id = get_customer_id()
#     #get servicing area
#     servicing_area = af.get_customer_servicing_area(customer_id)
#     #get courier id
#     courier_id = get_courier_id(servicing_area)
#     #compiling order_dict
#     order_dict = {"courier_id":courier_id,"customer_id":customer_id,"order_status": "New"}
#     #get order_id
#     order_id = get_order_id(order_dict)
#     #attach products to order_id
#     order_products_list = get_order_products(order_id,customer_id,courier_id)
#     #print(order_products_list) #REMEMBER TO COMMENT OUT!!!
#     os.system("clear")
#     #inserting order into order_prod db
#     af.insert_order_products(order_products_list)
#     #reducing stock by order amount
#     af.update_stock(order_products_list)
#     #add join to give customer an invoice with total
#     create_order_invoice(order_id)


# create_new_order()
from source.order_menu import order_status_catcher, print_order


####################################################################################################
###    PRiNT ORDERS FUNCTION
####################################################################################################
def display_orders():
    order_status = order_status_catcher()
    print_order(order_status)
    return True


display_orders()