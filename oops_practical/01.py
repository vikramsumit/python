import math

# 1. Convert temperature (Celsius <-> Fahrenheit)
def convert_temperature():
    choice = input("Convert to (C/F): ").upper()
    temp = float(input("Enter temperature: "))
    if choice == "C":
        print(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
    elif choice == "F":
        print(f"{temp}°C = {(temp * 9/5) + 32:.2f}°F")
    else:
        print("Invalid choice")

# 2. Gross Salary calculation
def gross_salary():
    basic = float(input("Enter basic salary: "))
    da = float(input("Enter DA: "))
    hr = float(input("Enter HR: "))
    print("Gross Salary =", basic + da + hr)

# 3. Check Odd/Even
def odd_even():
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")

# 4. Max and Min of 3 numbers
def max_min_three():
    a, b, c = map(int, input("Enter 3 numbers: ").split())
    print("Maximum =", max(a, b, c))
    print("Minimum =", min(a, b, c))

# 5. Print integers in ascending order
def ascending_order():
    nums = sorted(map(int, input("Enter numbers separated by space: ").split()))
    print("Ascending Order:", nums)

# 6. Prime factors of n
def prime_factors():
    n = int(input("Enter a number: "))
    i, factors = 2, []
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        factors.append(n)
    print("Prime Factors:", factors)

# 7. Co-prime check
def coprime():
    a, b = map(int, input("Enter two numbers: ").split())
    print(f"{a} and {b} are", "Co-Prime" if math.gcd(a, b) == 1 else "NOT Co-Prime")

# 8. Binary equivalent using recursion
def to_binary(n):
    return "" if n == 0 else to_binary(n // 2) + str(n % 2)

def binary_equivalent():
    n = int(input("Enter a positive number: "))
    print("Binary =", "0" if n == 0 else to_binary(n))

# ----------------------------
# Menu system
# ----------------------------
def main():
    options = {
        1: convert_temperature,
        2: gross_salary,
        3: odd_even,
        4: max_min_three,
        5: ascending_order,
        6: prime_factors,
        7: coprime,
        8: binary_equivalent
    }

    while True:
        print("\n--- MENU ---")
        print("1. Convert Temperature")
        print("2. Gross Salary")
        print("3. Odd/Even")
        print("4. Max/Min of 3 numbers")
        print("5. Ascending Order")
        print("6. Prime Factors")
        print("7. Co-prime Check")
        print("8. Binary Equivalent")
        print("9. Exit")

        choice = int(input("Enter choice: "))
        if choice == 9:
            print("Exiting...")
            break
        options.get(choice, lambda: print("Invalid choice!"))()

# Run program
if __name__ == "__main__":
    main()


# Output:
'''raju@kali:~/code only/python/oops_practical % python3 01.py

--- MENU ---
1. Convert Temperature
2. Gross Salary
3. Odd/Even
4. Max/Min of 3 numbers
5. Ascending Order
6. Prime Factors
7. Co-prime Check
8. Binary Equivalent
9. Exit
Enter choice: 1
Convert to (C/F): F
Enter temperature: 26
26.0°C = 78.80°F

Enter choice: 2
Enter basic salary: 55600
Enter DA: 20300
Enter HR: 8888
Gross Salary = 84788.0

Enter choice: 3
Enter a number: 558
Even

Enter choice: 4
Enter 3 numbers: 235 336 888
Maximum = 888
Minimum = 235

Enter choice: 5
Enter numbers separated by space: 21 36 33 45 658 546
Ascending Order: [21, 33, 36, 45, 546, 658]

Enter choice: 6
Enter a number: 562
Prime Factors: [2, 281]

Enter choice: 7
Enter two numbers: 265 4869
265 and 4869 are Co-Prime

Enter choice: 8
Enter a positive number: 654
Binary = 1010001110

Enter choice: 9
Exiting...'''