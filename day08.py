def greet():
    print("Hello, welcome to day 8!")

greet()

def greet_person(name):
    print(f"Hello, {name}! Hi there!")

greet_person("Alice")

def add(a, b):
    return a + b

result = add(3, 5)
print("Result:", result)

def add(a, b):
    print(a + b)

add(40, 4)

def introduce(name, job="Engineer"):
    print(f"My name is {name} and I am a {job}.")

introduce("Bob")
introduce("Charlie", "Doctor")

def efficiency(units, scrap):
    good_units = units - scrap
    return (good_units / units) * 100

print("Efficiency:", efficiency(100, 5), "%")       

def square(x):
    return x * x

print("Square of 6:", square(6))


def is_even(n):
    if n % 2 == 0:
        return True
    
print("Is 4 even?", is_even(4))


def machine_info(id, type):
    print(f"Machine ID: {id}, Type: {type}")

machine_info(101, "Lathe")

def multiply(a, b=2):
    return a * b

print("Multiply 5 by default:", multiply(5))

def average(numbers):
    return sum(numbers) / len(numbers)

print("Average:", average([10, 20, 30, 40]))