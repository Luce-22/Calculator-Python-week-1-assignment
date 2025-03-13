num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
operation = input("+, -, *, or /")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2 
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 !=0: 
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Invalid operation. Please enter a +, -, *, or /"

print(f"Result: {result}")

