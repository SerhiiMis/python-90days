# Day 5 - Dictionaries

machine = {
    "id": "M001",
    "type": "PLC",
    "status": "Running",
    "units": 120
}

print(machine["id"])        # M001
print(machine["status"])      # PLC

# Safe access
print(machine.get("location", "Unknown"))  # Unknown


machine["location"] = "Line 1"
machine["units"] = 150
del machine["status"]

print(machine)  # {'id': 'M001', 'type': 'PLC', 'units': 150, 'location': 'Line 1'}

for key, value in machine.items():
    print(f"{key}: {value}")

for k in machine.keys():
    print(k)

for v in machine.values():
    print(v)

factory = {
    "M001": {"type": "PLC", "status": "Running", "units": 150},
    "M002": {"type": "HMI", "status": "Idle", "units": 0},
    "M003": {"type": "SCADA", "status": "Running", "units": 300}
}

print(factory["M001"]["type"])  # PLC