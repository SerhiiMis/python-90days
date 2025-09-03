# Day 3 - Lists

machines = ["PLC", "HMI", "SCADA", "Sensor"]

print(machines)            # ['PLC', 'HMI', 'SCADA', 'Sendor']
print(machines[0])         # PLC        
print(machines[-1])       # Sensor
print(machines[1:3])      # ['HMI', 'SCADA']

machines[1] = "Panel"
print(machines)            # ['PLC', 'Panel', 'SCADA', 'Sensor']

machines.append("Robot")
print(machines)            # ['PLC', 'Panel', 'SCADA', 'Sensor', 'Robot']

machines.insert(2, "Drive")
print(machines)            # ['PLC', 'Panel', 'Drive', 'SCADA', 'Sensor', 'Robot']

machines.remove("PLC")
last = machines.pop()
print(machines)            # ['Panel', 'Drive', 'SCADA', 'Sensor']
print("Removed:", last)    # Removed: Robot


numbers = [5, 2, 9, 1, 7]

print(len(numbers))       # 5
print(min(numbers))       # 1
print(max(numbers))       # 9   
print(sum(numbers))       # 24

numbers.sort()         # Sorts the list in place
print(numbers)       # [1, 2, 5, 7, 9]

numbers.reverse()      # Reverses the list in place
print(numbers)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])        # [1, 2, 3]
print(matrix[2][1])     # 8



