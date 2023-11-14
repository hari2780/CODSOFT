import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)
    
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except (SyntaxError, ZeroDivisionError, TypeError):
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
temp_frame = tk.Frame(root, width=273, height=385)
temp_frame.pack_propagate(False)
temp_frame.pack()
window_width = temp_frame.winfo_reqwidth()
window_height = temp_frame.winfo_reqheight()
x_position = (root.winfo_screenwidth() - window_width) // 2
y_position = (root.winfo_screenheight() - window_height) // 2
temp_frame.destroy()
root.geometry(f'{window_width}x{window_height}+{x_position}+{y_position}')
entry = tk.Entry(root, width=16, font=('Arial', 20), borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
for button in buttons:
    text, row, column = button
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 16), command=calculate).grid(row=row, column=column)
    elif text == 'C':
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 16), command=clear_entry).grid(row=row, column=column)
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 16), command=lambda value=text: button_click(value)).grid(row=row, column=column)
root.mainloop()
