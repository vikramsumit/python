#  Create a Complex class to represent complex numbers with attributes for the real and imaginary parts. Overload the + operator to add two complex numbers.

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return Complex(real, imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(3, 4)
c2 = Complex(1, 2)
c3 = c1 + c2
# print(c3)
print(c1 + c2)