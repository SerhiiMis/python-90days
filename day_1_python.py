cars_produces = 1050
factory_location ="Detroit Assembly Plant"
defect_rate = 0.025
is_running = True

print("Welcome to the manufacturing dashboard.")
print(f"Today's production: {cars_produces} cars.")

expected_defects = cars_produces * defect_rate
print(f"Based on historical data, we expect approximately {expected_defects} defects today.")

if is_running:
    print("Production line is active. All systems are go.")
else:
    print("Production line is offline. Maintenance required.")

