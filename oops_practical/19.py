# Create a Car class with attributes for make, model, and year. Add a method to calculate the car's age based on the current year.

from datetime import datetime

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def age(self):
        current_year = datetime.now().year
        return current_year - self.year

car = Car("TATA", "Sierrs", 2025)
print(f"Car age: {car.age()} years")