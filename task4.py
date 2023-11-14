import tkinter as tk
from tkinter import ttk,messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors Game")
        self.master.geometry("600x400")
        self.master.configure(bg='#d3ffd3')
        self.user_score = 0
        self.computer_score = 0
        self.tree = ttk.Treeview(master, columns=('User Choice', 'Computer Choice', 'Result'), show='headings')
        self.tree.heading('User Choice', text='User Choice')
        self.tree.heading('Computer Choice', text='Computer Choice')
        self.tree.heading('Result', text='Result')
        self.tree_scroll = ttk.Scrollbar(master, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)
        self.tree.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")
        self.tree_scroll.grid(row=0, column=4, sticky="ns")
        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_choice_var = tk.StringVar()
        self.user_choice_var.set(self.choices[0])
        self.user_choices_menu = ttk.Combobox(master, textvariable=self.user_choice_var, values=self.choices, state="readonly")
        self.user_choices_menu.grid(row=1, column=0, pady=10)
        self.play_button = ttk.Button(master, text="Play", command=self.play_game)
        self.play_button.grid(row=1, column=1, pady=10)
        self.end_round_button = ttk.Button(master, text="End Round", command=self.end_round, state=tk.DISABLED)
        self.end_round_button.grid(row=1, column=2, pady=10)
        self.play_again_button = ttk.Button(master, text="Play Again", command=self.play_again, state=tk.DISABLED)
        self.play_again_button.grid(row=1, column=3, pady=10)
        self.score_label = ttk.Label(master, text="Score: User - 0 | Computer - 0", font=("Helvetica", 12))
        self.score_label.grid(row=2, column=0, columnspan=4, pady=10)

    def play_game(self):
        user_choice = self.user_choice_var.get()
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, result)
        self.update_score(result)
        self.update_score_label()
        self.play_again_button.config(state=tk.NORMAL)
        self.end_round_button.config(state=tk.NORMAL)
        self.tree.yview_moveto(1)  # Auto-scroll down

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            return "User"
        else:
            return "Computer"

    def display_result(self, user_choice, computer_choice, result):
        self.tree.insert("", "end", values=(user_choice, computer_choice, result))

    def update_score(self, result):
        if result == "User":
            self.user_score += 1
        elif result == "Computer":
            self.computer_score += 1

    def update_score_label(self):
        self.score_label.config(text=f"Score: User - {self.user_score} | Computer - {self.computer_score}")

    def play_again(self):
        self.tree.delete(*self.tree.get_children())
        self.play_again_button.config(state=tk.DISABLED)
        self.end_round_button.config(state=tk.DISABLED)

    def end_round(self):
        if self.user_score > self.computer_score:
            winner = "User"
        elif self.user_score < self.computer_score:
            winner = "Computer"
        else:
            winner = "Tie"

        messagebox.showinfo("Round End", f"The winner of the round is: {winner}")
        self.play_again()
        
root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
