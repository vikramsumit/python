import tkinter as tk
from tkinter import messagebox

# Functions for calculator operations
def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        label_result.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Math Error", "Division by zero is not allowed.")
        else:
            result = num1 / num2
            label_result.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create and place widgets
label1 = tk.Label(window, text="Enter first number:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

label2 = tk.Label(window, text="Enter second number:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

label_result = tk.Label(window, text="Result:")
label_result.grid(row=2, column=0, columnspan=2)

# Add buttons for operations
button_add = tk.Button(window, text="Add", command=add)
button_add.grid(row=3, column=0)

button_subtract = tk.Button(window, text="Subtract", command=subtract)
button_subtract.grid(row=3, column=1)

button_multiply = tk.Button(window, text="Multiply", command=multiply)
button_multiply.grid(row=4, column=0)

button_divide = tk.Button(window, text="Divide", command=divide)
button_divide.grid(row=4, column=1)

# Start the main loop
window.mainloop()
