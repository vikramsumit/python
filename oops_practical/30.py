# Shape Sorting with Inheritance:Implement a program that creates a list of various shapes (e.g., circles, rectangles, triangles) and sorts them based on their areas using inheritance. Each shape should have a method to calculate its area, and you should use inheritance to create specialized shape classes.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [
    Circle(5), 
    Rectangle(4, 6),
    Triangle(3, 8),
    Circle(3),
    Rectangle(2, 10)
]

shapes.sort(key=lambda shape: shape.area())

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")
