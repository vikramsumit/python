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

# OUTPUT:
# Price: $12.99
# Price: $8.99
# Price: $6.99

# Create an abstract class "PaymentGateway" with abstract methods for payment-related operations like process_payment() and refund_payment(). Create concrete subclasses for different payment gateways (e.g., "PayPal," "Stripe") and implement these methods to interact with the respective payment systems.

from abc import ABC, abstractmethod

class PaymentGateway:
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund_payment(self, amount):
        pass

class Paypal(PaymentGateway):
    def process_payment(self, amount):
        print(f"processing payment of ${amount} via Paypal.....")
        return True
    
    def refund_payment(self, amount):
        print(f"Processing refund of ${amount} via Paypal.....")
        return True
    
class Stripe(PaymentGateway):
    def process_payment(self, amount):
        print(f"processing payment of ${amount} via Stripe.....")
        return True
    
    def refund_payment(self, amount):
        print(f"Processing refund of ${amount} via Stripe.....")
        return True
    
paypal = Paypal()
paypal.process_payment(5000)
paypal.refund_payment(4500)

stripe = Stripe()
stripe.process_payment(80000)
stripe.refund_payment(80000)

# output:
# raju@kali:~/code only/python/oops_practical % python3 37.py
# processing payment of $5000 via Paypal.....
# Processing refund of $4500 via Paypal.....
# processing payment of $80000 via Stripe.....
# Processing refund of $80000 via Stripe.....

# Write a program for Division by zero Exception Handling.

try:
    num1 = 10
    num2 = 0
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# OUTPUT:
# Error: ision by zero is not allowed.





# Take a user-defined array and display it. Do exception handling, if array index out ofbound otherwise execute code when there is no error.

try:
    arr = [81, 22, 3, 4, 5,32,53,234,5,23,433,43,0]
    print("Array:", arr)
    
    index = 8
    print(f"Element at index {index}: {arr[index]}")
except IndexError:
    print(f"Error: Index {index} is out of bounds for array of length {len(arr)}.")
else:
    print("No error occurred. Code executed successfully.")

# OUTPUT:
# Array: [81, 22, 3, 4, 5, 32, 53, 234, 5, 23, 433, 43, 0]
# Element at index 8: 5
# No error occurred. Code executed successfully.


# Write a python programme to design a User Login page
import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid credentials!")

root = tk.Tk()
root.title("User Login")
root.geometry("300x150")

tk.Label(root, text="Username:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()






# Write a python program to design a student registration form
import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    roll = entry_roll.get()
    gender = gender_var.get()
    course = course_var.get()

    if name == "" or roll == "":
        messagebox.showerror("Error", "Please fill all required fields")
    else:
        messagebox.showinfo(
            "Registration Successful",
            f"Name: {name}\nRoll No: {roll}\nGender: {gender}\nCourse: {course}"
        )
def clear_form():
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    gender_var.set("")
    course_var.set("Select Course")
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x350")

tk.Label(root, text="Student Registration Form", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Student Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()
tk.Label(root, text="Roll Number").pack()
entry_roll = tk.Entry(root)
entry_roll.pack()
tk.Label(root, text="Gender").pack()
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Label(root, text="Course").pack()
course_var = tk.StringVar()
course_var.set("Select Course")

courses = ["BCA", "BSc", "BCom", "BA", "MCA"]
tk.OptionMenu(root, course_var, *courses).pack()

tk.Button(root, text="Submit", command=submit_form, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Clear", command=clear_form, bg="red", fg="white").pack()

root.mainloop()