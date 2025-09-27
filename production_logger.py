import csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("production_log.csv")

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = LOG_FILE.exists()
    
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Event"])
        writer.writerow([timestamp, event])

def read_log():
    if not LOG_FILE.exists():
        print("No log file found.")
        return

    with open(LOG_FILE, "r") as f:
        reader = csv.DictReader(f)
        print("\n--- Production Log ---")
        for row in reader:
            print(f"{row['Timestamp']} - {row['Event']}")


def main():
    print("Production Logger (CSV) started (type 'exit' to finish).")
    while True:
        event = input("Enter event: ")
        if event.lower() == 'exit':
            break
        log_event(event)

    read_log()


if __name__ == "__main__":
    main()

