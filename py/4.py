total_sum = 0

while True:
    user_input = input("no daal: ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        total_sum += number
    except ValueError:
        print("Please valid number.")

print("Total sum of entered numbers:", total_sum)
