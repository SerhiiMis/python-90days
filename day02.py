# Day 2 - Numbers

a = 10 # integer
b = 3.5 # float

# Basic operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus -> Remainder:", a % b)
print("Exponentiation -> 100:", a ** 2)

# Useful built-in functions
print("Absolute value:", abs(-7.5))
print("Round value:", round(3.14159, 2))
print("Power function -> 10^3:", pow(a, 3))
print("Minimum value:", min(5, 10, -3, 7))
print("Maximum value:", max(5, 10, -3, 7))

# Day 2 - Strings

text = "Python is awesome!"

# Concatenation
greeting = "Hello, " + text
print(greeting)

# f-strings (recommended)
name = "Serhii"
age = 36
print(f"My name is {name} and I am {age} years old.")

# Indexing and slicing
print(text[0])        # P
print(text[-1])       # !
print(text[0:6])  # Python
print(text[7:])  # awesome!

# String methods
print(text.upper())      # PYTHON IS AWESOME!
print(text.lower())      # python is awesome!
print(text.replace("awesome", "great"))  # Python is great!
print(text.split)   # ['Python', 'is', 'awesome!'] <built-in method split of str object at 0x0000026849E846B0>
print("Length of text:", len(text))  # 18
print("awesome" in text, "great" in text)  # True False

# Exercise 1
x = 15
y = 4
print((x + y), (x - y), (x * y), (x // y))

# Exercise 2
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}. You are {age} years old.")

# Exercise 3
message = "Industrial Python"
print(message[0:3])
print(message[-3:])
print(message.upper())
print("Python" in message)