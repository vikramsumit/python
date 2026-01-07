# Circle Class: Create a Circle class with an attribute for the radius. Add methods to calculate the area and circumference of the circle.
import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi* self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
    
radius = float(input("Enter the radius of circle: "))

circle = Circle(radius)

print(f"Area: {circle.area():.2f}")
print(f"Circumference: {circle.circumference():.3f}")