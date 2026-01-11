# Design a **Food delivery system** — for that, create an abstract class
# “MenuItem” with an abstract method “price” for common library operations
# like display price. Derive concrete classes for various item types, such as
# `Pizza`, `Burger`, `Momos`. Display the price for each item. 

from abc import ABC, abstractmethod

class MenuItem(ABC):
    @abstractmethod
    def price(self):
        pass

    def display_price(self):
        print(f"Price: ${self.price()}")

class Pizza(MenuItem):
    def price(self):
        return 12.99

class Burger(MenuItem):
    def price(self):
        return 8.99

class Momos(MenuItem):
    def price(self):
        return 6.99

pizza = Pizza()
burger = Burger()
momos = Momos()

pizza.display_price()
burger.display_price()
momos.display_price()