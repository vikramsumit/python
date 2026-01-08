# Bank Account Constructor: Extend the bank account example from a previous exercise (Exercise 2 in the previous response) to include a constructor that sets the account holder's name and initial balance.

class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}.\nNie balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}.\nNew balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

account = BankAccount("Raju Bhai", 5000)
account.withdraw(2500)
account.deposit(5555)