# Loop through a list
machines = ["PLC", "HMI", "SCADA"]
for m in machines:
    print("Machine:", m)

# Loop through a range of numbers
for i in range(5):
    print("i =", i)   # 0,1,2,3,4

# While Loops
count = 0
while count < 3:
    print("Count =", count)
    count += 1

# break → stop loop early
for i in range(10):
    if i == 5:
        break
    print(i)   # 0..4

# continue → skip this iteration
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)   # 1, 3, 5


# Nested Loops
for x in [1, 2]:
    for y in [10, 20]:
        print(x, y)
# Output:
# 1 10
# 1 20
# 2 10
# 2 20

# Loops with Dictionaries
factory = {
    "M001": {"type": "PLC", "units": 120},
    "M002": {"type": "Robot", "units": 80}
}

for machine_id, info in factory.items():
    print(machine_id, "->", info["type"], "produced", info["units"], "units")


