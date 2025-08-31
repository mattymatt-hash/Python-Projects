"""
* Name         : program name gui assignment
* Author       : Matthew Stevens
* Created      : Creation Date 7-9-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to write a number guessing game. The input is the user interaction when they push a button. The output is a response of if they were correct or not when it comes to there guess.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""         
import tkinter as tk
from tkinter import messagebox
import random
from number_guesser import NumberGuesser 

MAX = 10 
buttons = []
correct_number = 0
guesser = NumberGuesser()

def start_game():
    global correct_number
    correct_number = random.randint(1, MAX)
    guesser.reset()

    for btn in buttons:
        btn.config(state="normal", bg="SystemButtonFace")

def make_guess(n):
    guesser.add_guess(n)
    if n == correct_number:
        messagebox.showinfo("Winner", f"Correct! The number was {correct_number}")
        start_game()  # Restart 
    else:
        buttons[n - 1].config(state="disabled", bg="gray")

# Create GUI
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("600x400") # starting size

# this will define where the layout starts and how it expands to fill the screen when the user wants the gui bigger
total_columns = 5
total_rows = (MAX // total_columns) + (1 if MAX % total_columns else 0) + 1

for col in range(total_columns):
    window.grid_columnconfigure(col, weight=1)

for row in range(total_rows):
    window.grid_rowconfigure(row, weight=1) 

# Start button
start_btn = tk.Button(window, text="New Game / Start Over", command=start_game, bg="green", fg="white")
start_btn.grid(row=0, column=0, columnspan=total_columns, sticky="nsew",  padx=5, pady=5)

# Create number
for i in range(1, MAX + 1):
    row = ((i - 1) // total_columns) + 1
    col = (i - 1) % total_columns
    btn = tk.Button(window, text=str(i), command=lambda n=i: make_guess(n))
    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
    buttons.append(btn)

window.mainloop()

