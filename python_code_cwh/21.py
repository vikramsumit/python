def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
    
# factorial(54)
# factorial(5/4)
# factorial(5-4)
print(factorial(5*4))
print(factorial(5))
factorial(4)

def fibonacci(n):
    if (n == 0 or n  == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(10))