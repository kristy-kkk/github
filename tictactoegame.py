# Import tkinter module for GUI (Graphical User Interface)
import tkinter as tk

# Import messagebox to show popup messages (like winner alert)
from tkinter import messagebox

# Function to check if any player has won
def check_winner():

    # All possible winning combinations (row, column, diagonal)
    for combo in[
        [0, 1, 2],  # First row
        [3, 4, 5],  # Second row
        [6, 7, 8],  # Third row
        [0, 3, 6],  # First column
        [1, 4, 7],  # Second column
        [2, 5, 8],  # Third column
        [0, 4, 8],  # Main diagonal
        [2, 4, 6]   # Anti diagonal
    ]:
        
        # Check if all three buttons have same text (X or O) and are not empty
        if (
           buttons [combo[0]]['text'] == 
           buttons [combo[1]]['text'] == 
           buttons[combo[2]] ['text'] !=''
        ):
            
           # Highlight winning buttons in green
            buttons[combo[0]].config(bg='green')
            buttons[combo[1]].config(bg='green')
            buttons[combo[2]].config(bg='green')

             # Show popup message announcing the winner
            messagebox.showinfo(
                'Tic-Tac-Toe',
                f'Player {buttons[combo[0]]['text']} wins!'
            )

             # Close the game window
            root.quit()
            
# Function called when any button is clicked       
def button_click(index):

    # Check if button is empty and game is not finished
    if buttons[index]['text'] == '' and not winner:

        # Put current player's symbol (X or O)
        buttons[index]['text'] = current_player

        # Check if this move wins the game
        check_winner()

        # Change player turn
        toggle_player()

# Function to change player from X to O or O to X
def toggle_player():
    global current_player

    # Switch player
    current_player = 'x' if current_player == '0' else '0'
    
    # Update label text
    label.config (text = f"player {current_player}'s turn")

# create main application window
root = tk.Tk()

# Set window title
root.title ("Tic-Tac-Toe")

# Create 9 buttons for the game board
buttons = [
    tk.Button (
        root, text="",     #Initially empty
        font={"norml",25}, # Font Style and Size
        width = 6,
        height=2,
        command=lambda i=i: button_click(i) # Pass button index
    )
    for i in range(9)
]

#Place buttons in 3x3 grid
for i, button in enumerate (buttons):
    button.grid (row=i //3, column=i % 3)

#Initial player
current_player = "x"

# Winner flag (used to stop playing after win)
winner = False

#Label to show curent player's turn
label = tk.Label (
    root,
    text=f"Player {current_player}'s turn",
    font={"normal", 16}
)

# Place label below buttons
label.grid (row=3, column=0, columnspan=3)

#Start the GUI event Loop
root.mainloop()