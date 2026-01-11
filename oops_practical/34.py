# Bank Account Abstract Class:Design an abstract class "BankAccount" with abstract methods for common banking operations like deposit(), withdraw(), and get_balance(). Create concrete subclasses for various account types, such as "SavingsAccount," "CheckingAccount," and "FixedDepositAccount," and implement these methods accordingly.

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance=0):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass

class SavingsAccount(BankAccount):
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

class CheckingAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew ${amount}. Balance: ${self.balance}")

    def get_balance(self):
        return self.balance

class FixedDepositAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        print("Cannot withdraw from fixed deposit.")

    def get_balance(self):
        return self.balance

savings = SavingsAccount(1000)
savings.deposit(500)
savings.withdraw(200)
print(f"Savings balance: ${savings.get_balance()}")

checking = CheckingAccount(500)
checking.withdraw(600)
print(f"Checking balance: ${checking.get_balance()}")