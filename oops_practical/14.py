'''Create a online shopping cart system using inheritance.
Design a base class "Product" and derived class for various product categories (e.g. "Electronics", "Clothing", "Books").
Implement methods for adding removing items from the cart and calculating the total price with appropriate discounts for each category.'''

from dataclasses import dataclass
from typing import List, Optional

# ---------------------- Products ----------------------
class Product:
    """
    Base Product class.
    Subclasses should override get_discount(quantity) to return discount amount (absolute ₹).
    """
    def __init__(self, sku: str, name: str, price: float):
        self.sku = sku
        self.name = name
        self.price = float(price)

    def get_discount(self, quantity: int = 1) -> float:
        """
        Return total discount amount for the given quantity (in currency units).
        Default: no discount.
        """
        return 0.0

    def __str__(self):
        return f"{self.name} ({self.sku}) - ₹{self.price:.2f}"


class Electronics(Product):
    """
    Electronics: example discount = flat 5% off the electronics item(s).
    """
    def __init__(self, sku: str, name: str, price: float, warranty_years: int = 1):
        super().__init__(sku, name, price)
        self.warranty_years = warranty_years

    def get_discount(self, quantity: int = 1) -> float:
        return 0.05 * self.price * quantity  # 5% off per item


class Clothing(Product):
    """
    Clothing: example rule = 10% off when buying 2 or more of the same clothing item.
    """
    def __init__(self, sku: str, name: str, price: float, size: Optional[str] = None):
        super().__init__(sku, name, price)
        self.size = size

    def get_discount(self, quantity: int = 1) -> float:
        if quantity >= 2:
            return 0.10 * self.price * quantity  # 10% off total for this clothing item
        return 0.0


class Book(Product):
    """
    Book: example rule = flat ₹50 off per book when buying 3 or more copies of the same title.
    (Illustrative only — realistic stores rarely let you buy multiple identical books.)
    """
    def __init__(self, sku: str, name: str, price: float, author: Optional[str] = None):
        super().__init__(sku, name, price)
        self.author = author

    def get_discount(self, quantity: int = 1) -> float:
        if quantity >= 3:
            return 50.0 * quantity  # ₹50 off each when buying 3 or more
        return 0.0


# ---------------------- Cart & CartItem ----------------------
@dataclass
class CartItem:
    product: Product
    quantity: int = 1

    def line_total(self) -> float:
        return self.product.price * self.quantity

    def line_discount(self) -> float:
        return self.product.get_discount(self.quantity)


class ShoppingCart:
    def __init__(self):
        self.items: List[CartItem] = []

    def _find_item(self, sku: str) -> Optional[CartItem]:
        for item in self.items:
            if item.product.sku == sku:
                return item
        return None

    def add_product(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        existing = self._find_item(product.sku)
        if existing:
            existing.quantity += quantity
        else:
            self.items.append(CartItem(product, quantity))

    def remove_product(self, sku: str, quantity: int = None) -> bool:
        """
        Remove a product by SKU. If quantity is None or >= existing quantity, remove item completely.
        Returns True if something was removed, False if SKU not found.
        """
        item = self._find_item(sku)
        if not item:
            return False
        if quantity is None or quantity >= item.quantity:
            self.items.remove(item)
        else:
            if quantity <= 0:
                raise ValueError("Quantity must be positive when specified.")
            item.quantity -= quantity
        return True

    def update_quantity(self, sku: str, quantity: int) -> bool:
        """
        Set the quantity of an existing item. If quantity <= 0, the item is removed.
        Returns True if updated/removed, False if SKU not found.
        """
        item = self._find_item(sku)
        if not item:
            return False
        if quantity <= 0:
            self.items.remove(item)
        else:
            item.quantity = quantity
        return True

    def subtotal(self) -> float:
        return sum(item.line_total() for item in self.items)

    def total_discount(self) -> float:
        return sum(item.line_discount() for item in self.items)

    def total(self, tax_percent: float = 0.0) -> float:
        sub = self.subtotal()
        disc = self.total_discount()
        taxed = (sub - disc) * (1 + tax_percent / 100.0)
        return max(0.0, taxed)

    def itemized_bill(self) -> str:
        lines = []
        for item in self.items:
            p = item.product
            lines.append(
                f"{p.name} x{item.quantity} @ ₹{p.price:.2f} = ₹{item.line_total():.2f}"
                + (f"  (discount: -₹{item.line_discount():.2f})" if item.line_discount() else "")
            )
        lines.append(f"Subtotal: ₹{self.subtotal():.2f}")
        lines.append(f"Total discount: -₹{self.total_discount():.2f}")
        lines.append(f"Total (no tax): ₹{self.subtotal() - self.total_discount():.2f}")
        return "\n".join(lines)

    def checkout(self, tax_percent: float = 0.0) -> str:
        total_amt = self.total(tax_percent)
        receipt = self.itemized_bill()
        receipt += f"\nTax: {tax_percent:.2f}%\nGrand Total: ₹{total_amt:.2f}"
        # Optionally clear cart after checkout:
        self.items.clear()
        return receipt

    def is_empty(self) -> bool:
        return len(self.items) == 0


# ---------------------- Demo / Sample usage ----------------------
if __name__ == "__main__":
    # create some products
    phone = Electronics("E1001", "Smartphone X", 29999.0, warranty_years=2)
    tshirt = Clothing("C2001", "Graphic T-Shirt", 499.0, size="L")
    jeans = Clothing("C2002", "Blue Jeans", 1199.0, size="32")
    novel = Book("B3001", "Python for Everybody", 799.0, author="Dr. X")
    textbook = Book("B3002", "Algorithms (2nd Ed)", 1200.0, author="Prof. Y")

    cart = ShoppingCart()

    # add items
    cart.add_product(phone, 1)
    cart.add_product(tshirt, 3)   # triggers clothing discount (10% since qty >=2)
    cart.add_product(jeans, 1)
    cart.add_product(novel, 3)    # triggers book discount (₹50 per book)
    cart.add_product(textbook, 1)

    # print itemized bill
    print("Itemized bill BEFORE checkout:")
    print(cart.itemized_bill())
    print()

    # checkout with 18% tax
    print("Checkout receipt (18% tax):")
    print(cart.checkout(tax_percent=18.0))
