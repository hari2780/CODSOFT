import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    if complexity == "Low":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def generate_password_button_click():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()
        password = generate_password(length, complexity)
        password_display.config(state=tk.NORMAL)
        password_display.delete(1.0, tk.END)
        password_display.insert(tk.END, password)
        password_display.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

window = tk.Tk()
window.title("Password Generator")
background_color = "#D1E5F0" 
window.configure(bg=background_color)
font_style = ("Helvetica", 14, "bold")
length_label = tk.Label(window, text="Password Length:", font=font_style)
length_label.pack(pady=5)
length_entry = tk.Entry(window, font=font_style)
length_entry.pack(pady=5)
complexity_label = tk.Label(window, text="Password Complexity:", font=font_style)
complexity_label.pack(pady=5)
complexity_var = tk.StringVar()
low_button = tk.Radiobutton(window, text="Low", variable=complexity_var, value="Low", font=font_style)
medium_button = tk.Radiobutton(window, text="Medium", variable=complexity_var, value="Medium", font=font_style)
high_button = tk.Radiobutton(window, text="High", variable=complexity_var, value="High", font=font_style)
low_button.pack()
medium_button.pack()
high_button.pack()
complexity_var.set("Medium")
generate_button = tk.Button(window, text="Generate Password", command=generate_password_button_click, font=font_style)
generate_button.pack(pady=10)
password_display_label = tk.Label(window, text="Generated Password:", font=font_style)
password_display_label.pack(pady=5)
password_display = tk.Text(window, height=1, width=30, state=tk.DISABLED, font=font_style)
password_display.pack(pady=5)
window.mainloop()
