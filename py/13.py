# WAP using while loop to reverse string and print it

string = input("Enter a string: ")

i = len(string) - 1

reversed_string = ""

while i >= 0:
    reversed_string += string[i]
    i -= 1  

print("Reversed string:", reversed_string)
