import csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("production_log.csv")

def create_entry(event, machine="General"):
    """Return a dict with timestamp, machine, and event"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"timestamp": timestamp, "machine": machine, "event": event}

def save_entry(entry):
    """Save entry to CSV, create file with header if missing"""
    try:
        file_exists = LOG_FILE.exists()
        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "machine", "event"])
            if not file_exists:
                writer.writeheader()
            writer.writerow(entry)
    except Exception as e:
        print(f"⚠️ Error while saving log: {e}")

def read_log():
    """Read the CSV log and print all entries"""
    try:
        if not LOG_FILE.exists():
            print("⚠️ No log file found.")
            return
        with open(LOG_FILE, "r") as f:
            reader = csv.DictReader(f)
            print("\n--- Production Log ---")
            for row in reader:
                print(f"{row['timestamp']} | {row['machine']} | {row['event']}")
    except Exception as e:
        print(f"⚠️ Error while reading log: {e}")

def main():
    print("📒 Production Logger (type 'exit' to finish, 'show' to display log)")
    while True:
        event = input("Enter event: ")
        if event.lower() == "exit":
            break
        if event.lower() == "show":
            read_log()
            continue
        machine = input("Enter machine (or press Enter for General): ")
        entry = create_entry(event, machine if machine else "General")
        save_entry(entry)

if __name__ == "__main__":
    main()
