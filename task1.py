import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.configure(bg="#333")
        self.style = ttk.Style()
        self.style.configure("TButton", background="#4CAF50", foreground="black", font=('Arial', 12))
        self.style.configure("TLabel", background="#333", foreground="white", font=('Arial', 16, 'bold'))  # Increase font size and make it bold
        self.style.configure("TEntry", fieldbackground="#555", font=('Arial', 12))
        self.style.configure("TListbox", background="#555", foreground="white", font=('Arial', 12))
        self.tasks = []
        title_label = ttk.Label(root, text="To-Do List App")
        title_label.pack(pady=10)
        self.task_entry = ttk.Entry(root, width=40, font=('Arial', 12))
        self.task_entry.pack(pady=10)
        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, font=('Arial', 12))
        self.task_listbox.pack(pady=10)
        self.remove_button = ttk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.tasks.append(f"{task} ({timestamp})")
            self.task_listbox.insert(tk.END, f"{task} ({timestamp})")
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
            self.save_tasks()

    def save_tasks(self):
        with open("todo_tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("todo_tasks.txt", "r") as file:
                for line in file:
                    self.tasks.append(line.strip())
                    self.task_listbox.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

root = tk.Tk()
app = TodoApp(root)
root.mainloop()
