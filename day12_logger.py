from datetime import datetime

def create_entry(event, machine="General"):
    """Return a dict with timestamp, machine, and event"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"timestamp": timestamp, "machine": machine, "event": event}

def save_entry(entry, filename="production_log.csv"):
    """Append a log entry to a CSV file"""
    import csv
    from pathlib import Path

    file_exists = Path(filename).exists()

    with open(filename, "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "machine", "event"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(entry)

def main():
    print("Production Logger with Functions (type 'exit' to finish).")
    while True:
        event = input("Enter event: ")
        if event.lower() == 'exit':
            break
        machine = input("Enter machine name (or press Enter for General): ")
        entry = create_entry(event, machine if machine else "General")
        save_entry(entry)

if __name__ == "__main__":
    main()


