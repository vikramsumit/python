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

