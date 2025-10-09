# A list of car parts on an assembly line
assembly_line_parts = ["chassis", "engine", "brakes", "wheels", "interior"]

# Accessing items in a list. The first item is at index 0.
first_part = assembly_line_parts[0]
print(f"The first part on the line is: {first_part}")

# Accessing the last item using a negative index
last_part = assembly_line_parts[-1]
print(f"The last part on the line is: {last_part}")

# Slicing a list to get a range of items
core_components = assembly_line_parts[1:4] # This gets items from index 1 up to (but not including) 4
print(f"The core components for assembly are: {core_components}")

# Adding a new part to the end of the list
assembly_line_parts.append("windshield")
print(f"New part added: {assembly_line_parts}")

# Inserting a part at a specific position (e.g., adding the battery after the engine)
assembly_line_parts.insert(2, "battery")
print(f"Part inserted at index 2: {assembly_line_parts}")

# Removing a part
assembly_line_parts.remove("interior")
print(f"Part removed: {assembly_line_parts}")

# Create a list of quality inspection results (e.g., pass/fail)
inspection_results = ["pass", "pass", "fail", "pass", "fail", "pass", "pass"]

print("Inspection Results:")
for result in inspection_results:
    print(f"- {result}")

# Let's check each car and its assembly position
for index, part in enumerate(assembly_line_parts):
    print(f"Position {index}: {part}")


# Mock data for temperature readings from a sensor (in Celsius)
temperature_readings = [22.5, 25.0, 25.8, 23.1, 22.9, 23.3, 22.7, 23.5, 25.6, 23.2]

# Let's perform a simple data check. A reading over 25.0 is a red flag.
hot_readings = []

for temp in temperature_readings:
    if temp > 25.0:
        hot_readings.append(temp)

if hot_readings:
    print("\n--- Warning: Abnormal Temperature Readings Detected! ---")
    print(f"Readings over 25.0*C: {hot_readings}")
else: 
    print("\nNo abnormal temperature readings detected. System is stable.")

