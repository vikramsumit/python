# WAP to cal factorial, enter by user usin g while loop

num = int(input("Enter a number: "))

factorial = 1
i = num

while i > 0:
    factorial *= i
    i -= 1  

print(f"The factorial of {num} is {factorial}")