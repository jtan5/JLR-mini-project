import json

with open('example.json','r') as file:
  my_content = json.load(file)
  

print(my_content)
print(type(my_content))

print(my_content['menu'])
print(type(my_content['menu']))

print(my_content['menu']['items'])
print(type(my_content['menu']['items']))



item_list = my_content['menu']['items']

id_list = []

for index, items in enumerate(item_list):
    print(f"The ID for the items are: {items['id']}")
    print(type(items))
    item_header = items.keys()
    item_header2 = list(item_header)
    print(f"Item header:{item_header2}")
    print(type(item_header2))
    print(item_header2[0])
    id_list.append(items['id'])
    
print(id_list)

# export_dict = {
#     'president': {
#         'name' : 'Zaphod Beeblebrox',
#         'species' : 'Betelgeusian'
#     }
# }

# with open('my_json_exercises.json', 'w') as file:
#     json.dump(export_dict,file,indent=4)