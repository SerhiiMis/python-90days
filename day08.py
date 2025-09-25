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