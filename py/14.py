# WAP TO print all odd no b/w two no enter by user using for loop

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Odd numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end=" ")
