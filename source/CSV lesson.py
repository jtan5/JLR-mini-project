import csv
import json

#opening as a list
# with open('data.txt') as file:
#     reader = csv.reader(file,delimiter=',')
#     print(reader)
#     print(type(reader))
#     for row in reader:
#         print(row)

#opening as a dict
lineslist =[]

with open('data.txt') as file:
    reader_dict = csv.DictReader(file,delimiter=',')
    print(reader_dict)
    print(type(reader_dict))
    for index, row in enumerate(reader_dict):
        print(row)
        print(type(row))
        lineslist.append(row)
        header = row.keys()
        print(f"the header is {header}")
print(lineslist)
        
#iterating through the list to work out the values without the keys
#for index, row in enumerate(lineslist):
    
        
#writing a single line to csv
# with open('new_data.csv','w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Jon',1234])
    
    
# my_list = [
#     ['Jon', 123],
#     ['Alex',456]
# ]
# writing as a list doesn't have the column names; has to be manually
# with open('new_data2.csv','w') as file:
#     writer = csv.writer(file)
#     for row in my_list:
#         writer.writerow(row)
        

#from documentation
# with open('people.csv', mode='w') as file:
#   fieldnames = ['first_name', 'last_name', 'age']
#   writer = csv.DictWriter(file, fieldnames=fieldnames)
#   writer.writeheader()
#   writer.writerow({
#     'first_name': 'Jan',
#     'last_name': 'Smith',
#     'age': 60
#   })
  
with open('people200.csv', mode='w') as file:
  #it is usual to hardset the filenames, as this defines the column order
  fieldnames = [' phone', 'name']
  writer = csv.DictWriter(file, fieldnames=fieldnames)
  writer.writeheader()
  for row in lineslist:
    writer.writerow(row)
