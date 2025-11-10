# 07_FileHandling - Python Learning Log

# 1️⃣ Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, this is my first file write!\n")
    file.write("Python file handling is easy.\n")

# 2️⃣ Reading from a File
with open("example.txt", "r") as file:
    content = file.read()
    print("📖 File Content:\n", content)

# 3️⃣ Appending to a File
with open("example.txt", "a") as file:
    file.write("Appending a new line.\n")

# 4️⃣ Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print("➡", line.strip())

# 5️⃣ Exception Handling with Files
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("❌ File not found!")

# 6️⃣ Working with CSV Files
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Samuel", 25])
    writer.writerow(["Alice", 30])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 7️⃣ Working with JSON Files
import json

person = {"name": "Samuel", "age": 25, "language": "Python"}

# Write JSON
with open("person.json", "w") as json_file:
    json.dump(person, json_file)

# Read JSON
with open("person.json", "r") as json_file:
    data = json.load(json_file)
    print("🧩 JSON Data:", data)
