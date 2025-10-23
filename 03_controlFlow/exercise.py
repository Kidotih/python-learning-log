# 03_ControlFlow - Python-Learning-Log

# 1️⃣ If / Else Statements
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 2️⃣ Elif (Multiple conditions)
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# 3️⃣ Nested Conditions
temperature = 30
if temperature > 0:
    if temperature < 25:
        print("It’s a warm day.")
    else:
        print("It’s hot!")
else:
    print("It’s freezing!")

# 4️⃣ For Loop
for i in range(5):
    print("Loop count:", i)

# 5️⃣ While Loop
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

# 6️⃣ Break & Continue
for num in range(1, 10):
    if num == 5:
        break  # stop the loop
    if num % 2 == 0:
        continue  # skip even numbers
    print("Odd number:", num)

# 7️⃣ Mini Practice: Even or Odd Checker
number = 7
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
