# 05_DataStructures - Python Learning Log

# 1️⃣ Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Adding and removing elements
fruits.append("orange")
fruits.remove("banana")
print(fruits)

# Accessing elements
print(fruits[0])  # first item
print(fruits[-1]) # last item

# Iterating through a list
for fruit in fruits:
    print("I like", fruit)

# 2️⃣ Tuples (Immutable lists)
colors = ("red", "green", "blue")
print(colors)
print(colors[1])

# 3️⃣ Sets (Unique, unordered)
numbers = {1, 2, 3, 3, 2}
print(numbers)  # duplicates removed

# Adding/removing elements
numbers.add(4)
numbers.remove(1)
print(numbers)

# 4️⃣ Dictionaries (Key-Value Pairs)
person = {"name": "Samuel", "age": 25, "country": "Kenya"}
print(person)

# Access and update
print(person["name"])
person["age"] = 26
print(person)

# Adding new key
person["language"] = "Python"
print(person)

# Iterating through dictionary
for key, value in person.items():
    print(key, ":", value)

# 5️⃣ Nested Data Structures
people = [
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 30}
]
for p in people:
    print(p["name"], "is", p["age"], "years old")

# 6️⃣ Mini Practice: Contact Book
contacts = {}
# Add contacts
contacts["John"] = "john@example.com"
contacts["Alice"] = "alice@example.com"

# Retrieve contact
print("John's email:", contacts.get("John"))

# List all contacts
for name, email in contacts.items():
    print(name, "->", email)
