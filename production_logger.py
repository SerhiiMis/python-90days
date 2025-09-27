from datetime import datetime

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("production_log.txt", "a") as f:
        f.write(f"{timestamp} - {event}\n")

def read_log():
    with open("production_log.txt", "r") as f:
        print("\n--- Production Log ---")
        for line in f:
            print(line.strip())


def main():
    print("Production Logger started (type 'exit' to finish).")
    while True:
        event = input("Enter event: ")
        if event.lower() == 'exit':
            break
        log_event(event)

    read_log()


if __name__ == "__main__":
    main()

