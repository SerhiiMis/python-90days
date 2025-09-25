a = "John"
b = 30
c = "a software developer"

print(f"My name is {a}, I am years {b} old, and I work as {c}.")


x = 12
y = 3.14

print(x + y, x - y, x * y, x / y, x // y, x % y, x ** 2)


message = "Industrial Python"

print(message.upper(), message[0:3], message[-3:])

machines = ["Netstal", "Arburg", "KraussMaffei", "Haitian", "Engel", "Sumitomo"]

for i in range(len(machines)):
    print(f'Machine {i+1}: {machines[i]}')

for i in range(1, 6):
    print(i)

count = 5 
while count > 0:
    print("Countdown:", count)
    count -= 1

for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in machines:
    if i == "Haitian":
        continue
    print(i)


factory = {
    "M001": {"type": "PLC", "units": 120},
    "M002": {"type": "Robot", "units": 80}
}

for machine_id, info in factory.items():
    print(machine_id, "produced", info["units"], "units")


for j in range(1, 4):
    for k in range(1, 4):
        print(f"{j} x {k} = {j*k}")

        