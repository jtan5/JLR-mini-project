my_dict = {
    'key1' : {
        'name': 'Rob',
        'age': '99',
        'net worth' : "£52",
        },
    'key2' : {
        'name': 'Richard',
        'age' : 30,
        'net worth' : "£599992",
        }
}


my_dict2 = {
    'ids': [10, 20],
    'people': [
        {
            'name': 'Alex',
            'phone': 123456
        },
        {
            'name': 'Jon',
            'phone': 456789
        }
    ]
}

print (my_dict2)

#he wants to see Name:Alex, Phone: number

for index, person in enumerate(my_dict2['people']):
    print(f"""ID \t{my_dict2['ids'][index]}\tName: {person['name']}\tPhone: {person['phone']}""")
    

    