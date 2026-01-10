class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.02):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest ${interest:.2f}. Balance: ${self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, name, balance=0, overdraft_limit=100):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
        else:
            print("Exceeded overdraft limit.")

class FixedDepositAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05, term=12):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
        self.term = term  # months 
        self.is_mature = False

    def withdraw(self, amount):
        if self.is_mature:
            super().withdraw(amount)
        else:
            print("Cannot withdraw before maturity.")

    def mature(self):
        self.is_mature = True
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Account matured. Added interest ${interest:.2f}. Balance: ${self.balance}")

# Example usage
savings = SavingsAccount("raju", 1000)
savings.deposit(500)
savings.add_interest()

checking = CheckingAccount("Babu", 200)
checking.withdraw(250)

fixed = FixedDepositAccount("Shyam", 5000)
fixed.mature()
fixed.withdraw(1000)