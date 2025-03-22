# matchcase statement

day = input("Enter a day of the week: ").lower()  # Input day in lowercase

match day:
    case "monday":
        print("Start of the work week!")
    case "tuesday":
        print("Second day of the work week.")
    case "wednesday":
        print("Middle of the week.")
    case "thursday":
        print("Almost the weekend.")
    case "friday":
        print("Last working day!")
    case "saturday" | "sunday":
        print("It's the weekend!")
    case _:
        print("Not a valid day!")
