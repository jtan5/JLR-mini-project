#example of playing with json

import json

my_dict = {
    'name':'Jon',
    'phone': 123456,
    'age' :99,
    'is_active' : True,
    'address': None,
    'friends' : [
        {
            'name': 'Bob',
            'phone' : 789443
        },
        {
            'name':'Henry',
            'phone': 763337
        }
    ]
    }

with open('my_json_data.json', 'w') as file:
    json.dump(my_dict,file,indent=4)
    
        
with open('my_json_data.json','r') as file:
  my_content = json.load(file)
  
print(type(my_content))
print(my_content)

print(my_content['friends'][0])

my_complex = [
    {
    'name':'Jon',
    'phone': 123456,
    'age' :99,
    'is_active' : True,
    'address': None,
    'friends' : [
        {
            'name': 'Bob',
            'phone' : 789443
        },
        {
            'name':'Henry',
            'phone': 763337
        }
    ]
    },
    {
    'name':'Edward',
    'phone': 789448,
    'age' :99,
    'is_active' : True,
    'address': None,
    'friends' : [
        {
            'name': 'Thomas',
            'phone' : 789443
        },
        {
            'name':'Emily',
            'phone': 763337
        }
    ]
    },
        {
    'name':'Bob',
    'phone': 789443,
    'age' :99,
    'is_active' : True,
    'address': None,
    'friends' : [
        {
            'name': 'Rachel',
            'phone' : 789443
        },
        {
            'name':'Topham',
            'phone': 763337
        }
    ]
    }
]
print(type(my_complex))
with open('my_json_data2.json', 'w') as file:
    json.dump(my_complex,file,indent=2)
    
print(my_complex[1]['friends'])
print(my_complex[1]['friends'][0])