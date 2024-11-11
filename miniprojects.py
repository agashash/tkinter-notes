#calculator project



""" import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        
        self.result_var = tk.StringVar()
        
        # Entry for displaying the expression/result
        self.entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)
        
        # Creating buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # Adding buttons to the grid
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        # Clear button
        tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear).grid(row=row_val, column=0, columnspan=4)

    def on_button_click(self, char):
    "Handles button click events."
        if char == '=':
            try:
                # Evaluate the expression and update the entry
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            # Update the entry with the pressed button
            current_text = self.result_var.get()
            new_text = current_text + str(char)
            self.result_var.set(new_text)

    def clear(self):
        "Clears the entry."
        self.result_var.set("")

# Create the main window
root = tk.Tk()
calculator = Calculator(root)

# Run the Tkinter main loop
root.mainloop() """

#create a digital clock using tkinter

""" import tkinter as tk
from time import strftime

# Create a function to update the time
def time():
    # Get the current time in HH:MM:SS format
    current_time = strftime('%I:%M:%S:%p')# %H id for 24 hrs format
    # Update the label with the current time
    clock_label.config(text=current_time)
    # Call this function again after 1000ms (1 second)
    clock_label.after(1000, time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
clock_label.pack(anchor='center')

# Call the time function to start the clock
time()

# Run the Tkinter main loop
root.mainloop()
"""

# create  calender using tkinter

""" import tkinter as tk
import calendar
from tkinter import ttk

def show_calendar():
    # Get the year and month from the Spinbox
    year = int(year_spinbox.get())
    month = int(month_spinbox.get())
    
    # Get the month's calendar as a string
    cal = calendar.month(year, month)
    
    # Display the calendar in the label
    cal_label.config(text=cal)

# Create the main window
root = tk.Tk()
root.title("Calendar")

# Create and pack the year label and Spinbox
year_label = tk.Label(root, text="Select Year:")
year_label.pack(pady=5)
year_spinbox = tk.Spinbox(root, from_=1900, to=2100, width=10)
year_spinbox.pack(pady=5)

# Create and pack the month label and Spinbox
month_label = tk.Label(root, text="Select Month:")
month_label.pack(pady=5)
month_spinbox = tk.Spinbox(root, from_=1, to=12, width=5)
month_spinbox.pack(pady=5)

# Create and pack the button to show the calendar
show_button = tk.Button(root, text="Show Calendar", command=show_calendar)
show_button.pack(pady=10)

# Create and pack the label that will display the calendar
cal_label = tk.Label(root, text="", font=('courier', 12), justify=tk.LEFT)
cal_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
"""

#create a tic tac toe game using tkinter

'''import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.config(bg="pink")

# Game variables
current_player = "X"  # Player 1 starts with X
player1_name = ""
player2_name = ""
buttons = [[None for _ in range(3)] for _ in range(3)]  # 3x3 grid

# Function to check for a win or a draw
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]
    
    # Check for a draw
    if all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        return "Draw"
    return None

# Function to handle button clicks
def on_button_click(row, col):
    global current_player

    if buttons[row][col]["text"] != "":
        return

    buttons[row][col]["text"] = current_player
    buttons[row][col].config(bg="lightgreen" if current_player == "X" else "lightblue")

    result = check_winner()
    if result:
        if result == "Draw":
            messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        else:
            winner_name = player1_name if result == "X" else player2_name
            messagebox.showinfo("Tic-Tac-Toe", f"Player {winner_name} ({result}) wins!")
        reset_game()
    else:
        current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j].config(bg="white")

# Function to start the game
def start_game():
    global player1_name, player2_name
    player1_name = player1_entry.get()
    player2_name = player2_entry.get()

    if not player1_name or not player2_name:
        messagebox.showwarning("Input Error", "Please enter both player names!")
        return

    player1_entry.config(state="disabled")
    player2_entry.config(state="disabled")
    start_button.config(state="disabled")

# Create and pack player name labels and entries
player1_label = tk.Label(root, text="Player 1 (X) Name:", font=("Arial", 14))
player1_label.grid(row=0, column=0, padx=10, pady=5)
player1_entry = tk.Entry(root, font=("Arial", 14))
player1_entry.grid(row=0, column=1, padx=10, pady=5)

player2_label = tk.Label(root, text="Player 2 (O) Name:", font=("Arial", 14))
player2_label.grid(row=1, column=0, padx=10, pady=5)
player2_entry = tk.Entry(root, font=("Arial", 14))
player2_entry.grid(row=1, column=1, padx=10, pady=5)

# Start button to confirm player names
start_button = tk.Button(root, text="Start Game", font=("Arial", 14), command=start_game, bg="lightgreen")
start_button.grid(row=2, column=0, columnspan=7, pady=10)

# Create the 3x3 grid of buttons for Tic-Tac-Toe
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 40), width=5, height=2,
                                  command=lambda row=i, col=j: on_button_click(row, col), bg="orange")
        buttons[i][j].grid(row=i + 3, column=j, padx=5, pady=5)

# Run the Tkinter main loop
root.mainloop()
'''
#create a traffic signal using tkinter

""" import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("4-Way Traffic Signal")

# Set the size of the window
root.geometry("400x400")

# Define directions (0 = North, 1 = East, 2 = South, 3 = West)
directions = ["North", "East", "South", "West"]
current_direction = 0  # Start with North

# Create the canvas to draw the roads
canvas = tk.Canvas(root, width=400, height=400, bg="gray")
canvas.pack()

# Draw the roads (horizontal and vertical)
canvas.create_rectangle(150, 0, 250, 400, fill="black")  # Vertical road
canvas.create_rectangle(0, 150, 400, 250, fill="black")  # Horizontal road

# Create circles in the center for the traffic signal
red_light = canvas.create_oval(180, 180, 220, 220, fill="gray")
yellow_light = canvas.create_oval(230, 180, 270, 220, fill="gray")
green_light = canvas.create_oval(130, 180, 170, 220, fill="gray")

# Direction Label
direction_label = tk.Label(root, text="North Signal is Green", font=("Arial", 14), bg="gray", fg="white")
direction_label.place(x=100, y=10)

# Function to update the traffic signal
def change_signal():
    global current_direction

    # Reset all lights to gray
    canvas.itemconfig(red_light, fill="gray")
    canvas.itemconfig(yellow_light, fill="gray")
    canvas.itemconfig(green_light, fill="gray")

    # Change light based on current direction
    if current_direction == 0:  # North
        canvas.itemconfig(green_light, fill="green")
        direction_label.config(text="North Signal is Green")
        current_direction = 1
        root.after(3000, change_signal)  # Stay green for 3 seconds
    elif current_direction == 1:  # East
        canvas.itemconfig(yellow_light, fill="yellow")
        direction_label.config(text="East Signal is Yellow")
        current_direction = 2
        root.after(1000, change_signal)  # Stay yellow for 1 second
    elif current_direction == 2:  # South
        canvas.itemconfig(red_light, fill="red")
        direction_label.config(text="South Signal is Red")
        current_direction = 3
        root.after(3000, change_signal)  # Stay red for 3 seconds
    elif current_direction == 3:  # West
        canvas.itemconfig(green_light, fill="green")
        direction_label.config(text="West Signal is Green")
        current_direction = 0
        root.after(3000, change_signal)  # Stay green for 3 seconds

# Start the traffic signal
change_signal()

# Run the Tkinter main loop
root.mainloop() """
