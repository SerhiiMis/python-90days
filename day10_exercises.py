with open("notes.txt", "w") as f:
    f.write("I have learned how to write to a file\n")
    f.write("I have learned how to read from a file\n")
    f.write("I have learned how to append to a file\n")


with open("notes.txt", "r") as f:
    for line in f:
        print("LINE:", line.strip())


def save_numbers(filename, numbers):
    with open(filename, "w") as f:
        for number in numbers:
            f.write(f"{number}\n")

def load_numbers(filename):
    numbers = []
    with open(filename, "r") as f:
        for line in f:
            numbers.append(int(line.strip()))

    print("Loaded numbers:", numbers)


save_numbers("numbers.txt", [5, 4, 12, 7, 9])

load_numbers("numbers.txt")