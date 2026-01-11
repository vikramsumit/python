import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# -------------------------------
# Fake database (for demo)
# -------------------------------
USERS_DB = {
    "admin": "admin123",
    "user": "user123"
}

# -------------------------------
# Main Application
# -------------------------------
class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secure Login System")
        self.geometry("900x500")
        self.resizable(False, False)
        self.configure(bg="#1e1e2e")

        self.show_password = False

        self.create_ui()

    # -------------------------------
    # UI Design
    # -------------------------------
    def create_ui(self):
        # Left panel (Design)
        left_frame = tk.Frame(self, bg="#6c63ff", width=350, height=500)
        left_frame.pack(side="left", fill="y")

        tk.Label(
            left_frame,
            text="Welcome Back!",
            font=("Helvetica", 26, "bold"),
            bg="#6c63ff",
            fg="white"
        ).place(x=50, y=150)

        tk.Label(
            left_frame,
            text="Login to continue\naccessing your dashboard",
            font=("Helvetica", 14),
            bg="#6c63ff",
            fg="white"
        ).place(x=50, y=210)

        # Right panel (Login Form)
        right_frame = tk.Frame(self, bg="#1e1e2e")
        right_frame.pack(expand=True, fill="both")

        tk.Label(
            right_frame,
            text="User Login",
            font=("Helvetica", 24, "bold"),
            bg="#1e1e2e",
            fg="white"
        ).pack(pady=40)

        # Username
        self.username_entry = self.create_entry(
            right_frame, "Username"
        )

        # Password
        self.password_entry = self.create_entry(
            right_frame, "Password", show="*"
        )

        # Show password checkbox
        self.show_var = tk.BooleanVar()
        show_pass = tk.Checkbutton(
            right_frame,
            text="Show Password",
            variable=self.show_var,
            command=self.toggle_password,
            bg="#1e1e2e",
            fg="white",
            activebackground="#1e1e2e",
            activeforeground="white",
            selectcolor="#1e1e2e"
        )
        show_pass.pack(pady=5)

        # Remember Me
        self.remember_var = tk.BooleanVar()
        remember = tk.Checkbutton(
            right_frame,
            text="Remember Me",
            variable=self.remember_var,
            bg="#1e1e2e",
            fg="white",
            activebackground="#1e1e2e",
            activeforeground="white",
            selectcolor="#1e1e2e"
        )
        remember.pack(pady=5)

        # Login Button
        login_btn = tk.Button(
            right_frame,
            text="LOGIN",
            font=("Helvetica", 14, "bold"),
            bg="#6c63ff",
            fg="white",
            width=20,
            relief="flat",
            command=self.login
        )
        login_btn.pack(pady=30)

        # Hover effects
        login_btn.bind("<Enter>", lambda e: login_btn.config(bg="#5848e5"))
        login_btn.bind("<Leave>", lambda e: login_btn.config(bg="#6c63ff"))

        # Footer
        tk.Label(
            right_frame,
            text="© 2026 Secure Systems Inc.",
            font=("Helvetica", 10),
            bg="#1e1e2e",
            fg="gray"
        ).pack(side="bottom", pady=10)

    # -------------------------------
    # Entry Widget Helper
    # -------------------------------
    def create_entry(self, parent, placeholder, show=None):
        frame = tk.Frame(parent, bg="#1e1e2e")
        frame.pack(pady=10)

        label = tk.Label(
            frame,
            text=placeholder,
            font=("Helvetica", 12),
            bg="#1e1e2e",
            fg="white"
        )
        label.pack(anchor="w")

        entry = tk.Entry(
            frame,
            font=("Helvetica", 14),
            width=30,
            show=show,
            bg="#2a2a3d",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        entry.pack(ipady=8)
        return entry

    # -------------------------------
    # Show / Hide Password
    # -------------------------------
    def toggle_password(self):
        if self.show_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    # -------------------------------
    # Login Logic
    # -------------------------------
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if username in USERS_DB and USERS_DB[username] == password:
            msg = f"Welcome, {username}!"
            if self.remember_var.get():
                msg += "\n(We will remember you)"
            messagebox.showinfo("Login Successful", msg)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

# -------------------------------
# Run App
# -------------------------------
if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
