class Integer:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        return Integer(self.value + other.value)

    def __str__(self):
        return str(self.value)

class Text:
    def __init__(self, s=""):
        self.s = s

    def __add__(self, other):
        return Text(self.s + other.s)

    def __str__(self):
        return self.s


# Testing
a = float(input("Enter first integer: "))
b = float(input("Enter second integer: "))
print("Integer addition:", a, "+", b, "=", a + b)

t1 = Text(input("Enter first string: "))
t2 = Text(input("Enter second string: "))
print("String concatenation:", t1, "+", "+", t2, "=", t1 + t2)
 
