# Online Shopping Cart: Create an online shopping cart system using inheritance. Design a base class "Product" and derived classes for various product categories (e.g., "Electronics," "Clothing," "Books"). Implement methods for adding/removing items from the cart and calculating the total price with appropriate discounts for each category.

# class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price 

class Electronics(Product):
    def get_discounted_price(self):
        return self.price * 0.9 # 10%

class Clothing(Product):
    def get_discounted_price(self):
        return self.price * 0.85  # 15% 

class Books(Product):
    def get_discounted_price(self):
        return self.price * 0.95  # 5% 

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def remove_item(self, product_name):
        self.items = [item for item in self.items if item.name != product_name]
        print(f"Removed {product_name} from cart.")

    def total_price(self):
        total = sum(item.get_discounted_price() for item in self.items)
        return total

cart = ShoppingCart()

laptop = Electronics("Laptop", 1000)
tshirt = Clothing("T-Shirt", 20)
book = Books("Python Book", 50)

cart.add_item(laptop)
cart.add_item(tshirt)
cart.add_item(book)

print(f"Total price: ${cart.total_price():.2f}")

cart.remove_item("T-Shirt")
print(f"New total: ${cart.total_price():.2f}")