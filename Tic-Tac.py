import tkinter as tk
from tkinter import messagebox

def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if button[combo[0]]["text"] == button[combo[1]]["text"] == button[combo[2]]["text"] != "":
            for idx in combo:
                button[idx].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {button[combo[0]]['text']} wins!")
            return True  # End game
    if all(btn["text"] != "" for btn in button):
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        return True  # End game
    return False

def button_click(index):
    global current_player, winner
    if button[index]["text"] == "" and not winner:
        button[index]["text"] = current_player
        if check_winner():
            winner = True
        else:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "o" if current_player == "x" else "x"
    label.config(text=f"Player {current_player}'s turn")

def reset_game():
    global winner
    for btn in button:
        btn.config(text="", bg="SystemButtonFace")
    current_player = "x"
    winner = False
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

button = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, btn in enumerate(button):
    btn.grid(row=i // 3, column=i % 3)

current_player = "x"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset Game", font=("normal", 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
