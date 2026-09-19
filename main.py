print("Welcome to my console calculator!\n")

def read_numbers(number):
    while True:
        try:
            return float(input(number))
        except ValueError:
            print("Please enter a number!")
a = read_numbers("Enter A: ")
b = read_numbers("Enter B: ")

print("Choice operations: [ + ][ - ][ * ][ / ]")

choice = (input("Enter your choice: "))
if "+" in choice:
    print("Result: ", a+b)
elif "-" in choice:
    print("Result: ", a-b)
elif "*" in choice:
    print("Result: ", a*b)
elif "/" in choice:
    print("Result: ", a/b)
else:
    print("Unknow operation")

