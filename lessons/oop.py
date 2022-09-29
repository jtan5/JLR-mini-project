num = int(123)

# model a Person type

class Person:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception
        self.name = name
        
    def __str__(self):
        return f'Class: Person\t({self.name})'
    

jane = Person("Jane Doe")

print(type(jane))
print(jane.name)
print(jane)

#type hinting eg: a:int  isn't enforced, its more for humans
def add_numbers(a: int, b: int) -> int:
    return a + b

print(add_numbers(1,3))

from nis import cat
from typing import List
class Cat:
    name="Sam"
    
    def meow(self):
        print(self.name + " says Meow")
        
c = Cat()
c.meow()

class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name)
        self.job_title = job_title
        print(f"My class is {self}")
        
    def describe_profession(self):
        return f"I work as a {self.job_title}"
    def __str__(self):
        return f'Class: Employee\t({self.name},{self.job_title})'
    
    
rebecca = Person("Becky")
print(rebecca)

e = Employee(rebecca.name, "Developer")
print(e)
print(e.describe_profession())