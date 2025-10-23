# 02_DataTypes - Python Learning Log

# 1️⃣ Integers and Floats
age = 21       # int
height = 5.9   # float
print("Age:", age)
print("Height:", height)

# 2️⃣ Strings
name = "Samuel"
language = 'Python'
print("Name:", name)
print("Language:", language)

# 3️⃣ Booleans
is_learning = True
is_tired = False
print("Is learning Python?", is_learning)
print("Is tired?", is_tired)

# 4️⃣ Checking data types
print(type(age))
print(type(height))
print(type(name))
print(type(is_learning))

# 5️⃣ Type Conversion
age_str = str(age)
print("Converted age:", age_str, "Type:", type(age_str))

# 6️⃣ String Operations
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Length of name:", len(name))
print("First letter:", name[0])

# 7️⃣ Combining data
message = f"My name is {name}, I am {age} years old, and I’m learning {language}."
print(message)

# 8️⃣ Try input (optional)
# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# print(f"Hello {user_name}, you are {user_age} years old.")
