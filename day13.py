# Lambda function: square a number
square = lambda x: x ** 2
print(square(5))  # 25

# Inline usage
print((lambda x, y: x + y)(3, 4))  # 7

units = [10, 20, 30, 40]

# Double each unit
doubled = list(map(lambda x: x*2, units))
print(doubled)  # [20, 40, 60, 80]

events = ["Running", "Stopped", "Error", "Running"]

# Only keep 'Running'
running_events = list(filter(lambda x: x=="Running", events))
print(running_events)  # ['Running', 'Running']

machines = [{"id": "M1", "units": 50}, {"id": "M2", "units": 120}]

# Sort by units produced
sorted_machines = sorted(machines, key=lambda x: x["units"])
print(sorted_machines)
# [{'id': 'M1', 'units': 50}, {'id': 'M2', 'units': 120}]

def apply_operation(numbers, func):
    return [func(n) for n in numbers]

nums = [1, 2, 3]
result = apply_operation(nums, lambda x: x**3)  # cube each number
print(result)  # [1, 8, 27]
