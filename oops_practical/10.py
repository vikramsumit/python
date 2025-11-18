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
