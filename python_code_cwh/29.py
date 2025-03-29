# Raising Custom Error

a = int(input(";Enter the no btw 3 and 65: "))

if(a<3 or a >65):
    raise ValueError("Enter no between 3 and 65")