# Product Constructor: Create a Product class with a constructor that initializes attributes for product name and price. Instantiate different products with varying details.

class Product:
    def __init__(self, product, name, price):
        self.product = product
        self.name = name
        self.price = price

product1 = Product("smartphone", "samsung s24", 55000)

print(f"{product1.product} - {product1.name} - {product1.price}")
        