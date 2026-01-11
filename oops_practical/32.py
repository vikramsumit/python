# Shape Area Calculation:
# Create a base class called "Shape" with a method calculate_area() that returns 0. Then, create derived classes for different shapes like "Circle," "Rectangle," and "Triangle." Override the calculate_area() method in each derived class to calculate and return the area of that specific shape.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

circle = Circle(6)
rectangle = Rectangle(4, 8)
triangle = Triangle(4, 18)

print(f"Circle area: {circle.calculate_area():.2f}")
print(f"Rectangle area: {rectangle.calculate_area()}")
print(f"Triangle area: {triangle.calculate_area()}")