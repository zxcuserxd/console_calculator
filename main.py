print("Welcome to my console calculator!/n")

a = float(input("Enter A: "))
b = float(input("Enter B: "))

print("Choice operations: + , - , * , /")
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

