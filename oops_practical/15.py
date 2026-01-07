'''Bank Account Inheritance: Design a class hierarchy for different types of bank acounts , such as saving accounts, checking accounts and fixed diposit account. 
Inplement common operations like deposits, withdrawls, and balance inquiries'''

from datetime import datetime, timedelta
from typing import Optional

class BankAccount:
    _next_account_number = 1000000

    def __init__(self, holder_name: str, balance: float = 0.0):
        self.account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1
        self.holder_name = holder_name
        self.balance = float(balance)

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> float:
        return self.balance

    def transfer_to(self, target: "BankAccount", amount: float) -> None:
        self.withdraw(amount)
        target.deposit(amount)

    def __str__(self):
        return f"Account[{self.account_number}] {self.holder_name}: ₹{self.balance:.2f}"
    
# ---------------- Savings Account ----------------
class SavingsAccount(BankAccount):
    def __init__(self, holder_name: str, balance: float = 0.0,
                 annual_interest_rate: float = 4.0,
                 min_balance: float = 500.0,
                 min_balance_penalty: float = 100.0):
        super().__init__(holder_name, balance)
        self.annual_interest_rate = float(annual_interest_rate)
        self.min_balance = float(min_balance)
        self.min_balance_penalty = float(min_balance_penalty)

    def withdraw(self, amount: float) -> float:
        new_balance = super().withdraw(amount)
        if new_balance < self.min_balance:
            self.balance -= self.min_balance_penalty
        return self.balance

    def accrue_interest(self, months: int = 1) -> float:
        if months <= 0:
            raise ValueError("Months must be positive.")
        interest = self.balance * (self.annual_interest_rate / 100.0) * (months / 12.0)
        self.balance += interest
        return interest
    
# ---------------- Checking Account ----------------
class CheckingAccount(BankAccount):
    def __init__(self, holder_name: str, balance: float = 0.0,
                 overdraft_limit: float = 0.0, overdraft_fee: float = 0.0):
        super().__init__(holder_name, balance)
        self.overdraft_limit = float(overdraft_limit)
        self.overdraft_fee = float(overdraft_fee)
        self._in_overdraft = False

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        potential_balance = self.balance - amount
        if potential_balance < -self.overdraft_limit:
            raise ValueError("Exceeds overdraft limit.")

        self.balance = potential_balance

        if self.balance < 0 and not self._in_overdraft and self.overdraft_fee > 0:
            self.balance -= self.overdraft_fee
            self._in_overdraft = True

        if self.balance >= 0:
            self._in_overdraft = False

        return self.balance
    
# ---------------- Fixed Deposit Account ----------------
class FixedDepositAccount:
    _next_fd_account = 9000000

    def __init__(self, holder_name: str, principal: float,
                 term_months: int, annual_interest_rate: float = 6.0,
                 start_date: Optional[datetime] = None,
                 early_withdrawal_penalty_pct: float = 50.0):
        if principal <= 0:
            raise ValueError("Principal must be positive.")
        if term_months <= 0:
            raise ValueError("Term must be positive months.")

        self.fd_account_number = FixedDepositAccount._next_fd_account
        FixedDepositAccount._next_fd_account += 1

        self.holder_name = holder_name
        self.principal = float(principal)
        self.term_months = int(term_months)
        self.annual_interest_rate = float(annual_interest_rate)
        self.start_date = start_date or datetime.now()
        self.early_withdrawal_penalty_pct = float(early_withdrawal_penalty_pct)
        self.is_closed = False 

    def maturity_date(self) -> datetime:
        return self.start_date + timedelta(days=30 * self.term_months)

    def _interest_for_term(self, months: Optional[int] = None) -> float:
        months = months if months is not None else self.term_months
        return self.principal * (self.annual_interest_rate / 100.0) * (months / 12.0)

    def is_matured(self, as_of: Optional[datetime] = None) -> bool:
        as_of = as_of or datetime.now()
        return as_of >= self.maturity_date()

    def withdraw(self, as_of: Optional[datetime] = None) -> float:
        if self.is_closed:
            raise ValueError("This fixed deposit is already closed.")
        as_of = as_of or datetime.now()
        if self.is_matured(as_of):
            interest = self._interest_for_term()
            payout = self.principal + interest
        else:
            elapsed_days = (as_of - self.start_date).days
            elapsed_months = max(0, elapsed_days // 30)
            interest = self._interest_for_term(elapsed_months)
            penalty = (self.early_withdrawal_penalty_pct / 100.0) * interest
            payout = self.principal + interest - penalty

        self.is_closed = True
        return payout

    def __str__(self):
        return (f"FD[{self.fd_account_number}] {self.holder_name}: Principal=₹{self.principal:.2f}, "
                f"Term={self.term_months} months, Rate={self.annual_interest_rate:.2f}%")

# ---------------- Example usage / Quick demo ----------------
if __name__ == "__main__":
    print("=== Bank Accounts Demo ===\n")

    sav = SavingsAccount("Raju", balance=2000.0, annual_interest_rate=4.5, min_balance=1000.0, min_balance_penalty=50.0)
    print("Created:", sav)
    print("Deposit 500 ->", sav.deposit(500))
    print("Accrue interest for 6 months -> interest added:", sav.accrue_interest(months=6))
    print("Balance after interest:", sav.get_balance())
    try:
        print("Withdraw 1800 ->", sav.withdraw(1800))
        print("Balance after withdrawal (may have penalty if below min):", sav.get_balance())
    except ValueError as e:
        print("Withdrawal failed:", e)
    print()

    chk = CheckingAccount("Shyam", balance=1000.0, overdraft_limit=500.0, overdraft_fee=100.0)
    print("Created:", chk)
    print("Withdraw 1200 (uses overdraft) ->", chk.withdraw(1200))
    print("Balance after overdraft and fee:", chk.get_balance())
    try:
        chk.withdraw(500) 
    except ValueError as e:
        print("Further withdrawal failed:", e)
    print()

    print("Transfer ₹200 from savings to checking")
    try:
        sav.transfer_to(chk, 200)
        print("Savings:", sav)
        print("Checking:", chk)
    except ValueError as e:
        print("Transfer failed:", e)
    print()

    fd = FixedDepositAccount("Babubhai", principal=10000.0, term_months=12, annual_interest_rate=7.0, early_withdrawal_penalty_pct=40.0)
    print("Created FD:", fd)
    print("Maturity date:", fd.maturity_date().date())
    
    early_date = fd.start_date + timedelta(days=30 * 4)
    payout_early = fd.withdraw(as_of=early_date)
    print(f"Early withdrawal payout after 4 months: ₹{payout_early:.2f}")


'''Create a online shopping cart system using inheritance.
Design a base class "Product" and derived class for various product categories (e.g. "Electronics", "Clothing", "Books").
Implement methods for adding removing items from the cart and calculating the total price with appropriate discounts for each category.'''

from dataclasses import dataclass
from typing import List, Optional

# ---------------------- Products ----------------------
class Product:
    def __init__(self, sku: str, name: str, price: float):
        self.sku = sku
        self.name = name
        self.price = float(price)

    def get_discount(self, quantity: int = 1) -> float:
        return 0.0
    
    def __str__(self):
        return f"{self.name} ({self.sku}) - ₹{self.price:.2f}"

class Electronics(Product):
    def __init__(self, sku: str, name: str, price: float, warranty_years: int = 1):
        super().__init__(sku, name, price)
        self.warranty_years = warranty_years

    def get_discount(self, quantity: int = 1) -> float:
        return 0.05 * self.price * quantity  

class Clothing(Product):
    def __init__(self, sku: str, name: str, price: float, size: Optional[str] = None):
        super().__init__(sku, name, price)
        self.size = size

    def get_discount(self, quantity: int = 1) -> float:
        if quantity >= 2:
            return 0.10 * self.price * quantity 
        return 0.0

class Book(Product):
    def __init__(self, sku: str, name: str, price: float, author: Optional[str] = None):
        super().__init__(sku, name, price)
        self.author = author

    def get_discount(self, quantity: int = 1) -> float:
        if quantity >= 3:
            return 50.0 * quantity  
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
        self.items.clear()
        return receipt
    
    def is_empty(self) -> bool:
        return len(self.items) == 0

# ---------------------- Demo / Sample usage ----------------------
if __name__ == "__main__":
    phone = Electronics("E1001", "Smartphone X", 29999.0, warranty_years=2)
    tshirt = Clothing("C2001", "Graphic T-Shirt", 499.0, size="L")
    jeans = Clothing("C2002", "Blue Jeans", 1199.0, size="32")
    novel = Book("B3001", "Python for Everybody", 799.0, author="Dr. X")
    textbook = Book("B3002", "Algorithms (2nd Ed)", 1200.0, author="Prof. Y")

    cart = ShoppingCart()

    cart.add_product(phone, 1)
    cart.add_product(tshirt, 3)   
    cart.add_product(jeans, 1)
    cart.add_product(novel, 3)    
    cart.add_product(textbook, 1)

    print("Itemized bill BEFORE checkout:")
    print(cart.itemized_bill())
    print()

    print("Checkout receipt (18% tax):")
    print(cart.checkout(tax_percent=18.0))