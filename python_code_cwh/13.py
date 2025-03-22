# def average(a,b,c=564):
#     # print(type(numbers))
#     print("The average is ", (a+b+c)/2)
    
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum/ len(numbers))
    return sum/ len(numbers)
    return 99
    
c = average(54.5,22,54,409.99)
print(c)

# def name(fname, mname, lname="bhai"):
#     print("Hello ",fname,mname,lname)

# name("peter","raju")
# name("nepali","kaju")
# name("pappu","jalebi")