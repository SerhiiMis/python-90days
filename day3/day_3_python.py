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