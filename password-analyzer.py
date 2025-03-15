import tkinter as tk
from tkinter import messagebox
import re
import hashlib

# Function to check password strength
def check_password_strength(password):
    strength = 0
    criteria = [
        (r"[a-z]", "Lowercase letter"),
        (r"[A-Z]", "Uppercase letter"),
        (r"[0-9]", "Digit"),
        (r"[!@#$%^&*()_+\-=\[\]{};:'\",.<>?/|]", "Special character"),  # Fixed escaping
        (r".{8,}", "At least 8 characters")
    ]
    
    met_criteria = [desc for pattern, desc in criteria if re.search(pattern, password)]
    strength = len(met_criteria)
    
    if strength == 5:
        return "Strong", met_criteria
    elif strength >= 3:
        return "Moderate", met_criteria
    else:
        return "Weak", met_criteria

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to toggle password visibility
def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_button.config(text="Hide")
    else:
        entry.config(show='*')
        toggle_button.config(text="Show")

# GUI application
def analyze_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password")
        return
    
    strength, met_criteria = check_password_strength(password)
    hashed = hash_password(password)
    
    result_label.config(text=f"Strength: {strength}\nMet Criteria: {', '.join(met_criteria)}\nHashed: {hashed}")

# GUI setup
root = tk.Tk()
root.title("Password Analyzer")
root.geometry("400x300")

label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

toggle_button = tk.Button(root, text="Show", command=toggle_password)
toggle_button.pack(pady=5)

button = tk.Button(root, text="Analyze", command=analyze_password)
button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
