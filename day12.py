def greet():
    print("Hello, engineer!")

greet()

def add_numbers(a, b):
    return a +b

print(add_numbers(3, 5))

def log_event(event, machine="Machine 1"):
    return f"{machine}: {event}"

print(log_event("Started"))
print(log_event("Stopped", machine="Machine 2"))

