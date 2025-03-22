try:
    hours = int(input("Enter the hour (0-23): "))
    minutes = int(input("Enter the minutes (0-59): "))
    seconds = int(input("Enter the seconds (0-59): "))

    if (hours < 0 or hours > 23) or (minutes < 0 or minutes > 59) or (seconds < 0 or seconds > 59):
        print("Invalid time! Please ensure the hours, minutes, and seconds are within valid ranges.")
    else:
        if 5 <= hours <= 11:
            print("Good morning")
        elif 12 <= hours <= 16:
            print("Good afternoon")
        elif 17 <= hours <= 20:
            print("Good evening")
        else:
            print("Good night")
except ValueError:
    print("Invalid input! Please enter valid integers for hours, minutes, and seconds.")
