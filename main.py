# This is a basic program to mark the start of my journey

# Adds 2 input numbers
def add(x, y):
    return x + y

# Subtracts 2 numbers
def subtract(x, y):
    return x - y

# Multiplies 2 numbers
def multiply(x, y):
    return x * y

# Divides 2 numbers
def divide(x, y):
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Taking input time
choice = input("Enter 1 - 4:")

# Check if the option entered is one of the available options
if choice in ('1' '2' '3' '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input!")