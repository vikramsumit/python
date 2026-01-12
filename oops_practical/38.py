# Write a program for Division by zero Exception Handling.

try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")