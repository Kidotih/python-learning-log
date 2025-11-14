🐍 PYTHON BASICS — CORE NOTES

1. Variables & Data Types

Python is dynamically typed — no need to declare types.

x = 10          # int
pi = 3.14       # float
name = "Sam"    # string
is_active = True  # boolean

Common Data Types
	•	int – whole numbers
	•	float – decimal numbers
	•	str – text
	•	bool – True/False
	•	list – ordered, changeable
	•	tuple – ordered, unchangeable
	•	set – unordered, unique items
	•	dict – key–value pairs

2. Operators

Arithmetic

+  -  *  /  %  //  **

Comparison

==  !=  >  <  >=  <=

Logical

and  or  not

3. Control Flow

If / Elif / Else

age = 20

if age >= 18:
    print("Adult")
elif age == 17:
    print("Almost there")
else:
    print("Minor")

4. Loops

For Loop

for i in range(5):
    print(i)

While Loop

count = 0
while count < 3:
    count += 1

5. Functions

Defining Functions

def greet(name):
    return f"Hello, {name}"

print(greet("Sam"))

Default Parameters

def add(a=0, b=0):
    return a + b

6. Lists

fruits = ["apple", "banana", "orange"]

fruits.append("mango")
fruits.remove("banana")

print(fruits[0])     # indexing
print(fruits[-1])    # negative indexing

List Comprehension

squares = [x*x for x in range(5)]

7. Dictionaries

user = {
    "name": "Sam",
    "age": 22,
}

print(user["name"])
user["country"] = "Kenya"

8. Sets

nums = {1, 2, 3, 3}
print(nums)   # duplicates removed

9. Tuples

coords = (10, 20)
# coords[0] = 30  # error (immutable)

10. Input & Output

name = input("Enter your name: ")
print("Hello", name)

11. Error Handling

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")

12. Working With Files

with open("data.txt", "r") as file:
    content = file.read()

with open("data.txt", "w") as file:
    file.write("Hello world")

13. Modules & Import

import math
print(math.sqrt(16))

Create your own module:

# utils.py
def add(a, b):
    return a + b

# main.py
from utils import add
print(add(2, 3))

14. Basic OOP

Class Definition

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"My name is {self.name}"

p = Person("Sam", 22)
print(p.speak())

15. Virtual Environments

python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

16. Pip Package Management