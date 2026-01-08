# Create a compute class with method overloading for area of circle and rectangle. The class should have a method called area() that takes variable arguments. Depending on the number of arguments, it should calculate either area of circle and rectangle  . 

import math

class Compute:
    def area(self, *args):
        if len(args) == 1:
            radius = args[0]
            return math.pi * radius ** 2
        elif len(args) == 2:
            length, width = args
            return length * width
        else:
            return "Invalid number of arguments."

comp = Compute()
print(f"Circle area: {comp.area(5):.2f}")
print(f"Rectangle area: {comp.area(4, 6)}")
