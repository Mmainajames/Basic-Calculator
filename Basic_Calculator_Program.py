# Basic Calculator Program

# Ask user for input
num1 = float(input("Enter the first number: "))
operation = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation based on operation
if operation == "+":
    result = num1 + num2
    print("num1 + num2 =", result)
elif operation == "-":
    result = num1 - num2
    print("num1 - num2 =", result)
elif operation == "*":
    result = num1 * num2
    print("num1 * num2 =", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("num1 / num2 =", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please use +, -, *, or /.")
