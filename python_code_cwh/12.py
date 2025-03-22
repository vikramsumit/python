def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print("The required geometric mean is", mean)
    
def isGreater(a, b):
    if a > b:
        print("a is greater")
    elif a == b:
        print("a is equal to b")
    else:
        print("b is greater than a")
        
def somefunction(a,b):
    pass

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

# if a > b:
#     print("a is greater")
# if a == b:
#     print("a is equal to b")  # Corrected comparison
# else:
#     print("b is greater than a")
isGreater(a, b)
calculateGmean(a, b)
# gmean = (a * b) / (a + b)
# print("The geometric mean is:", gmean)

# Second part
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

# if a > b:
#     print("a is greater")
# else:
#     print("b is greater or equal to a")
isGreater(a, b)
calculateGmean(a, b)
# gmean = (a * b) / (a + b)
# print("The geometric mean is:", gmean)
