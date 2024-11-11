#1. Basic Entry Usage:
""" 
Question:
Create a Tkinter application with an Entry widget that allows the user to input their age. Add a button that, when clicked, displays a message in a Label saying whether the user is an adult (age 18 and above) or a minor (under 18). 
"""
"""
import tkinter as tk
from tkinter import messagebox

def check_age():
    try:
        age = int(age_entry.get())  # Get the age from the Entry widget and convert to an integer
        if age >= 18:
            result_label.config(text="You are an adult.")
        else:
            result_label.config(text="You are a minor.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Age Checker")
root.geometry("300x200")
root.config(bg="skyblue")

# Create a Label for instructions
instruction_label = tk.Label(root, text="Please enter your age:")
instruction_label.pack(pady=10)

# Create an Entry widget for user input
age_entry = tk.Entry(root, width=10,fg="red")
age_entry.pack(pady=10)

# Create a Button to check the age
check_button = tk.Button(root, text="Check Age", command=check_age,bg="yellow")
check_button.pack(pady=10)

# Create a Label to display the result
result_label = tk.Label(root, text="",bg="skyblue",fg="black")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
"""

#2. Password Entry:
"""
Question:
Create a login form using Entry widgets where one field is for a username and the other is for a password. Make the password field masked (so the characters are hidden). When the user clicks the login button, display the entered username in a label but keep the password hidden.
"""
"""
import tkinter as tk

def login():
    # Get the values from the username and password entries
    username = username_entry.get()
    # Display the username in the result label, but do not display the password
    result_label.config(text=f"Welcome, {username}!")
    
# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

# Create a label and entry for the username
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

# Create a label and entry for the password (masked)
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, width=30, show="*")  # 'show="*"' masks the password input
password_entry.pack(pady=5)

# Create a login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

# Create a label to display the result (username after login)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
"""

#3. Multiple Entries:
""" 
Question:
Create a Tkinter form with three Entry widgets that ask for the user’s first name, last name, and email. When the user clicks a button, concatenate the first name and last name, and display a welcome message along with the entered email address in a label. 
"""
""" 
import tkinter as tk

def display_info():
    # Get the first name, last name, and email from the Entry widgets
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    
    # Concatenate the first and last names
    full_name = f"{first_name} {last_name}"
    
    # Display the welcome message and email
    result_label.config(text=f"Welcome, {full_name}!\nYour email: {email}")

# Create the main window
root = tk.Tk()
root.title("User Information Form")
root.geometry("400x300")

# Create a label and entry for the first name
first_name_label = tk.Label(root, text="First Name:")
first_name_label.pack(pady=5)
first_name_entry = tk.Entry(root, width=30)
first_name_entry.pack(pady=5)

# Create a label and entry for the last name
last_name_label = tk.Label(root, text="Last Name:")
last_name_label.pack(pady=5)
last_name_entry = tk.Entry(root, width=30)
last_name_entry.pack(pady=5)

# Create a label and entry for the email
email_label = tk.Label(root, text="Email:")
email_label.pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Create a button to display the welcome message
submit_button = tk.Button(root, text="Submit", command=display_info)
submit_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop() 
"""

#4. Entry Validation (Numbers Only):
""" 
Question:
Create a calculator application that takes two numbers from the user using two Entry widgets. Ensure that only numbers are allowed as input. If the user enters non-numeric characters, display an error message in a label. If the input is valid, show the sum of the two numbers. 
"""
""" 
import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        # Get the values from the Entry widgets
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        
        # Calculate the sum
        total = num1 + num2
        
        # Display the result in the result_label
        result_label.config(text=f"Sum: {total}")
    except ValueError:
        # Display an error message if input is not valid numbers
        result_label.config(text="Error: Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")

# Create a label and entry for the first number
num1_label = tk.Label(root, text="Enter first number:")
num1_label.pack(pady=5)
num1_entry = tk.Entry(root, width=20)
num1_entry.pack(pady=5)

# Create a label and entry for the second number
num2_label = tk.Label(root, text="Enter second number:")
num2_label.pack(pady=5)
num2_entry = tk.Entry(root, width=20)
num2_entry.pack(pady=5)

# Create a button to calculate the sum
calc_button = tk.Button(root, text="Calculate Sum", command=calculate_sum)
calc_button.pack(pady=10)

# Create a label to display the result or error
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop() 
"""


#5. Character Limit in Entry:
""" 
Create an Entry widget that allows the user to enter a name. Limit the input to a maximum of 10 characters. If the user exceeds this limit, display an error message below the Entry widget. The error message should disappear if the input is within the allowed range. 
"""
""" 
import tkinter as tk

def check_input(*args):
    name = name_var.get()
    # Check if the length of the input exceeds 10 characters
    if len(name) > 10:
        error_label.config(text="Error: Maximum 10 characters allowed")
    else:
        error_label.config(text="")  # Clear error message if input is within limit

# Create the main window
root = tk.Tk()
root.title("Character Limit Entry")
root.geometry("300x150")

# Create a StringVar to track the text in the Entry widget
name_var = tk.StringVar()
name_var.trace("w", check_input)  # 'trace' calls check_input whenever the content changes

# Create a label and entry for the name
name_label = tk.Label(root, text="Enter your name (max 10 characters):")
name_label.pack(pady=5)

name_entry = tk.Entry(root, textvariable=name_var, width=30)
name_entry.pack(pady=5)

# Create a label to display error messages
error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=5)

# Run the main loop
root.mainloop() 
"""
