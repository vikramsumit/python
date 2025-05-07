# PRACTISE
# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
    
# except IndexError:
#   print("Index Error")

# try:
#     num = int(input("Enter an integer: "))
# except ValueError:
#     print("Number entered is not an integer.")
# else:
#     print("Integer Accepted.")
# finally:
#     print("This block is always executed.")
    
# a = int(input("Enter any value between 5 and 9: \n"))

# if(a<5  or a>9):
#   raise  ValueError("Value should be between 5 and 9")

class CustomError(Exception):
    """Custom exception for invalid operations."""
    pass

def divide(a, b):
    if b == 0:
        raise CustomError("Division by zero is not allowed.")
    return a / b

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    
    result = divide(num1, num2)
    print(f"Result: {result}")

except CustomError as e:
    print(f"Custom Error: {e}")

except ValueError:
    print("Please enter valid integers.")
