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
