# Bank Account Class: Implement a BankAccount class with attributes for an account holder's name and balance. Add methods to deposit and withdraw money from the account.

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

account = BankAccount("JOhn wick", 1000)
account.deposit(500)
account.withdraw(200)

account2 = BankAccount("Raju Scammer", 2000)
account.deposit(5000)
account.withdraw(9000)