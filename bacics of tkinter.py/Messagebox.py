#1. Basic Message Box:
'''
Create a Tkinter application with a button labeled "Show Message". When the user clicks the button, display a message box that says "Hello, welcome to Tkinter!".
'''
""" import tkinter as tk
from tkinter import messagebox

def show_message():
    # Display the message box with a custom message
    messagebox.showinfo("Greeting", "Hello, welcome to Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Message Box Example")
root.geometry("300x200")

# Create a button that will show the message box when clicked
message_button = tk.Button(root, text="Show Message", command=show_message)
message_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop() """

#2. Confirmation Box:
""" Create a Tkinter application with a button labeled "Exit". When the user clicks the button, display a confirmation message box asking, "Are you sure you want to exit?". If the user selects "Yes", close the application. If the user selects "No", do nothing """

"""import tkinter as tk
from tkinter import messagebox

def confirm_exit():
    # Display a confirmation message box
    response = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
    
    # If the user clicks 'Yes', close the application
    if response:
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Confirmation Box Example")
root.geometry("300x200")

# Create an "Exit" button that will trigger the confirmation box
exit_button = tk.Button(root, text="Exit", command=confirm_exit)
exit_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()"""

#3. Error Message Box:
""" Create a Tkinter form with an entry field for the user to input their email address and a "Submit" button. If the user leaves the email field empty and clicks "Submit", display an error message box saying, "Email field cannot be empty!". """

"""import tkinter as tk
from tkinter import messagebox

def submit_email():
    # Get the content of the email entry field
    email = email_entry.get()
    
    # Check if the email field is empty
    if not email:
        # Show an error message if the field is empty
        messagebox.showerror("Error", "Email field cannot be empty!")
    else:
        # Display a message indicating successful submission
        messagebox.showinfo("Success", f"Email submitted: {email}")

# Create the main window
root = tk.Tk()
root.title("Email Form")
root.geometry("300x150")

# Create a label for the email field
email_label = tk.Label(root, text="Enter your email:")
email_label.pack(pady=10)

# Create an entry widget for email input
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Create a "Submit" button
submit_button = tk.Button(root, text="Submit", command=submit_email)
submit_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

"""

#4. Input Validation with Message Box:
""" Create a Tkinter form with two entry fields for the user to input a username and password. Add a "Login" button. When the user clicks "Login", check if the username or password fields are empty. If any field is empty, display a warning message box. If both fields are filled, display an information message box saying "Login Successful!".
"""

""" import tkinter as tk
from tkinter import messagebox

def validate_login():
    # Get the content of the username and password fields
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if either field is empty
    if not username or not password:
        # Show a warning message if any field is empty
        messagebox.showwarning("Warning", "Username or Password cannot be empty!")
    elif username==u_name and password==u_pass:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        # Show a success message if both fields are filled
        messagebox.showerror("Error", "Please Enter the valid Username and Password")

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

#set username and password
u_name="a123"
u_pass="123"

# Create a label for username
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=5)

# Create an entry widget for username input
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

# Create a label for password
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=5)

# Create an entry widget for password input, with masking
password_entry = tk.Entry(root, width=30, show='*')
password_entry.pack(pady=5)

# Create a "Login" button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
"""

#5. Quiz Application with Message Box Feedback:
""" 
Create a quiz application with one question and four answer options using radio buttons. When the user selects an answer and clicks "Submit", display a message box indicating whether the answer is correct or incorrect. 
"""

""" 
import tkinter as tk
from tkinter import messagebox

def submit_answer():
    # Get the selected answer
    selected_option = answer_var.get()

    # Check if the selected answer is correct
    if selected_option == "2":
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showerror("Result", "Incorrect!")

# Create the main window
root = tk.Tk()
root.title("Quiz Application")
root.geometry("400x300")

# Create a label for the question
question_label = tk.Label(root, text="What is the capital of France?", font=("Arial", 14))
question_label.pack(pady=20)

# Create a variable to store the selected answer
answer_var = tk.StringVar(value="0")  # Default value (no selection)

# Create radio buttons for the answer options
option1 = tk.Radiobutton(root, text="Berlin", variable=answer_var, value="1", font=("Arial", 12))
option2 = tk.Radiobutton(root, text="Paris", variable=answer_var, value="2", font=("Arial", 12))
option3 = tk.Radiobutton(root, text="Madrid", variable=answer_var, value="3", font=("Arial", 12))
option4 = tk.Radiobutton(root, text="Rome", variable=answer_var, value="4", font=("Arial", 12))

# Pack the radio buttons
option1.pack(pady=5)
option2.pack(pady=5)
option3.pack(pady=5)
option4.pack(pady=5)

# Create a "Submit" button
submit_button = tk.Button(root, text="Submit", command=submit_answer)
submit_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop() 
"""

