try:
    number = int("abc")  # This will fail
except ValueError:
    print("Oops! That was not a number.")

try:
    num = 10 / 0 
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid value.")

try: 
    num = int("42")
except ValueError:
    print("Not a number!")
else:
    print("Conversion successful:", num)
finally:
    print("This always runs.")

def load_units(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
            return int(data)
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("File does not  contain a number.")
    finally:
        print("Finished attempting to load units.")

print(load_units("units.txt"))


