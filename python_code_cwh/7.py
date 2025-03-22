# conditional statement

# a = int( input( "Enter your age: "))
# print( "Your age is: " , a)

# Conditional operators
# >, <, >=, <=, == >!=
# print(a>18)
# print(a<= 18)
# print(a==18)
# print(a!= 18)

# if(a > 18):
#     print("you can drink and drive")
# else:
#     print("you cannot drive")
#     print("you cannot drive")
# print("you ccnnot drive")

# if statement
x = 10
if x > 5:
    print("x is greater than 5")  # This block will execute
    
# if else statement
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")  # This block will execute

# if elif else statement
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")  # This block will execute
else:
    print("x is less than 5")

# nested if means double if statement
age = 15
gpa = 8
extracurriculars = ["sports", "volunteering"]

if age >= 18:  # Check if age is 18 or above
    if gpa >= 3.5:  # Check if GPA is 3.5 or above
        if "sports" in extracurriculars:  # Check if involved in sports
            if "volunteering" in extracurriculars:  # Check if involved in volunteering
                print("Eligible for Full Scholarship")  # All conditions met
            else:
                print("Eligible for Partial Scholarship")  # Missing volunteering but others are met
        else:
            if "volunteering" in extracurriculars:
                print("Eligible for Partial Scholarship")  # Missing sports but others are met
            else:
                print("Eligible for Basic Scholarship")  # No sports or volunteering
    else:
        if gpa >= 3.0:
            print("Eligible for Basic Scholarship")  # Lower GPA but still qualifies for basic
        else:
            print("Not Eligible for Scholarship")  # Low GPA disqualifies
else:
    if age < 18 and gpa >= 3.5:
        print("Eligible for Junior Scholarship")  # Younger but has good GPA
    else:
        print("Not Eligible for Scholarship")  # Too young and doesn't meet GPA requirements

# conditional
x = 10
result = "Greater" if x > 5 else "Smaller or Equal"
print(result)  # Outputs "Greater"

# statement with logics
x = 10
y = 5

# Using 'and'
if x > 5 and y < 10:
    print("Both conditions are True")  # This block will execute

# Using 'or'
if x > 15 or y < 10:
    print("At least one condition is True")  # This block will execute

# Using 'not'
if not x < 5:
    print("x is not less than 5")  # This block will execute


my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("3 is in the list")  # This block will execute
