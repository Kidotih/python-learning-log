# 04_Functions - Python Learning Log
# Complete coverage of functions in Python

# 1️⃣ Defining a Simple Function
def greet(name):
    print("Hello,", name)

greet("Samuel")
greet("Python Learner")

# 2️⃣ Function with Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# 3️⃣ Function with Default Arguments
def greet(name="Friend"):
    print("Hello,", name)

greet()
greet("Alice")

# 4️⃣ Function with Multiple Arguments
def multiply(a, b, c):
    return a * b * c

print("Product:", multiply(2, 3, 4))

# 5️⃣ Keyword Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Samuel")

# 6️⃣ Variable Scope
x = 10  # global variable

def change_x():
    global x
    x = 20
    print("Inside function:", x)

change_x()
print("Outside function:", x)

# 7️⃣ Arbitrary Number of Arguments (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum of all:", sum_all(1, 2, 3, 4, 5))

# 8️⃣ Arbitrary Keyword Arguments (**kwargs)
def person_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

person_info(name="Samuel", age=25, country="Kenya")

# 9️⃣ Nested Functions
def outer_function(msg):
    def inner_function():
        print("Message inside inner function:", msg)
    inner_function()

outer_function("Hello from nested function!")

# 🔟 Lambda Functions (Anonymous Functions)
square = lambda x: x**2
print("Square of 5:", square(5))

# 1️⃣1️⃣ Docstrings
def multiply(a, b):
    """
    Multiply two numbers and return the result.
    """
    return a * b

print(multiply(3, 4))
print(multiply.__doc__)

# 1️⃣2️⃣ Mini Practice: Calculator Function
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"

print(calculator(10, 5, "add"))
print(calculator(10, 5, "divide"))
