'''Write a class compute where area of rectangel/square by using method overloading'''

class Compute:
    def area(self, *args):
        if len(args) == 1:
            side = args[0]
            return side * side # Square: 1 argument
        elif len(args) == 2:
            length, breadth = args
            return length * breadth # Rectangle: 2 arguments
        else:
            return "Invalid number of arguments"

c = Compute()

choice = int(input("Enter 1 for square area, 2 for rectangle area: "))

if choice == 1:
    arsq =float(input("Enter side length for square: "))
    print("Area of square :", c.area(arsq))

elif choice == 2:
    arrec_length = float(input("Enter length for rectangle: "))
    arrec_breadth = float(input("Enter breadth for rectangle: "))
    print("Area of rectangle :", c.area(arrec_length, arrec_breadth))
else:
    print("Invalid choice")

'''Write a program to perform addition and concatination using operator overloading'''
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

a = float(input("Enter first integer: "))
b = float(input("Enter second integer: "))
print("Integer addition:", a, "+", b, "=", a + b)

t1 = Text(input("Enter first string: "))
t2 = Text(input("Enter second string: "))
print("String concatenation:", t1, "+", "+", t2, "=", t1 + t2)
 
'''Write a program of addition of two complex number using Binary+(binary +operator overlaoding)'''
class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"

c1 = Complex(3.5, 2)
c2 = Complex(1.5, -4)
print("c1 =", c1)
print("c2 =", c2)
print("c1 + c2 =", c1 + c2)

'''Perform addition of two complex numbers using constructor overloading'''
class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    @classmethod
    def add(cls, c1, c2):
        """Simulating constructor overloading for addition"""
        return cls(c1.real + c2.real, c1.imag + c2.imag)
    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"

x = Complex(2, 3)
y = Complex(1.5, -1)

sum_complex = Complex.add(x, y)

print("x =", x)
print("y =", y)
print("Sum =", sum_complex)

