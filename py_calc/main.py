print("Calculator in Python!")
print("Select operation.")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

choice = input("Enter operation: ")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        if num2 == 0:
            print("Division by 0 is not possible")
        else:
            print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid Input")