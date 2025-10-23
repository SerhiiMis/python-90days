# Day 4 - Tuples and Sets

# Tuples 
coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])      

# Cannot change values
# coordinates[0] = 15  # This will raise an error

# Tuple unpacking
x, y = coordinates
print(f"x: {x}, y: {y}")

# Sets
machines = {"PLC", "HMI", "SCADA", "PLC"} # Duplicates are ignored
print(machines)  # {'HMI', 'PLC', 'SCADA'}

# Membership test
print("HMI" in machines)  # True
print("Sensor" in machines)  # False

# Add / Remove
machines.add("Robot")
machines.remove("HMI")
print(machines)  # {'Robot', 'PLC', 'SCADA'}

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Union: {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersection: {3, 4}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric Difference: {1, 2, 5, 6}

# Mini-exercises
tuple_ex = (5, 10, 15)
print(tuple_ex[1])  # 10
a, b, c = tuple_ex
print(f"a: {a}, b: {b}, c: {c}")
