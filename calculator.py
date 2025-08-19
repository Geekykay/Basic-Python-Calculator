# This is a basic calculator for the Power Learn Project Assignment
# This Python program would allow user perform basic aritimetic operations with ease!

# Let's outline the steps:
# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")

# It's time to do the math! Let's run some calculations.

# Perform the operation based on user input
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation.")


# Now we have a basic calculator program !!