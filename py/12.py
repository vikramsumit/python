# WAP to print table of no using for loop

num = int(input("Enter a number: "))

print(f"Multiplication Table of {num}:")

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")


