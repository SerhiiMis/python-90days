with open("log.txt", "w") as f:
    f.write("Production started\n")
    f.write("Machine A online\n")


with open("log.txt", "r") as f:
    content = f.read()
    print(content)


with open("log.txt", "a") as f:
    f.write("Machine B online\n")


with open("log.txt", "r") as f:
    for line in f:
        print("LINE:", line.strip())


# Factory log
def log_event(event):
    with open("factory_log.txt", "a") as f:
        f.write(event + "\n")

log_event("Start shift")
log_event("Machine 1 error")
log_event("End shift")

# Read back
with open("factory_log.txt", "r") as f:
    print(f.read())



