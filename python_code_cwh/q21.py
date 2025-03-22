# from datetime import datetime

# Get the current system time
# current_time = datetime.now()

# Extract hours, minutes, and seconds
# hours = current_time.hour
# minutes = current_time.minute
# seconds = current_time.second

hours = int(input("Enter the hour (0-23): "))
minutes = int(input("Enter the minutes (0-59): "))
seconds = int(input("Enter the seconds (0-59): "))


# Print the current time (optional)
print(f"Current Time: {hours:02}:{minutes:02}:{seconds:02}")

# Determine the appropriate greeting based on the hour
if 5 <= hours <= 11:
    print("Good morning")
elif 12 <= hours <= 16:
    print("Good afternoon")
elif 17 <= hours <= 20:
    print("Good evening")
else:
    print("Good night")
