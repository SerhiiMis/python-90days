component_data = {
    "part_id": "PN-4001",
    "name": "Brake Caliper",
    "assembly_station": 4,
    "quality_status": "PASS",
    "cycle_time_sec": 45.2,
    "is_critical": True
}

part_name = component_data["name"]
print(f"Part being inspected: {part_name}")

component_data["quality_status"] = "REWORK"
print(f"Updated status: {component_data['quality_status']}")

component_data["inspector_id"] = 105
print(f"Inspector ID added: {component_data['inspector_id']}")

print("\n--- Component Details ---")
for key, value in component_data.items():
    print(f"{key.replace('_', ' ').title()}: {value}")

def get_station_label(station_number):
    """Returns the descriptive name for an assembly station number."""
    if station_number == 1:
        return "Chassis Build"
    elif station_number == 4:
        return "Brake Installation"
    else:
        return "General Assembly"

station = component_data["assembly_station"]
label = get_station_label(station)
print(f"\nPart is at station {station}, which is the: {label}")
