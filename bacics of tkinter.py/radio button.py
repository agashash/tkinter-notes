#1. Basic Radio Button Selection:
"""
Create a Tkinter application with three radio buttons labeled "Option 1", "Option 2", and "Option 3". When the user selects an option and clicks a "Submit" button, display the selected option in a label. 
"""
""" import tkinter as tk

def submit_choice():
    # Get the selected option from the radio button group
    selected_option = option_var.get()
    # Update the label to display the selected option
    result_label.config(text=f"You selected: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Basic Radio Button Selection")
root.geometry("300x200")

# Create a variable to store the selected radio button value
option_var = tk.StringVar()

# Set a default value for the radio buttons
option_var.set("Option 1")

# Create radio buttons
radio1 = tk.Radiobutton(root, text="Option 1", variable=option_var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=option_var, value="Option 2")
radio3 = tk.Radiobutton(root, text="Option 3", variable=option_var, value="Option 3")

# Pack the radio buttons
radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_choice)
submit_button.pack(pady=10)

# Create a label to display the selected option
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
"""

#2. Pizza Size Selection:
""" 
Create a form with three radio buttons to select the size of a pizza: "Small", "Medium", and "Large". When the user selects a size and clicks a "Submit" button, display a message in a label like "You selected: Large pizza."
"""
""" 
import tkinter as tk

def submit_choice():
    # Get the selected option from the radio button group
    selected_option = option_var.get()
    # Update the label to display the selected option
    result_label.config(text=f"You selected: {selected_option}  pizza")

# Create the main window
root = tk.Tk()
root.title("Basic Radio Button Selection")
root.geometry("300x200")

# Create a variable to store the selected radio button value
option_var = tk.StringVar()

# Set a default value for the radio buttons
option_var.set("Small")

# Create radio buttons
radio1 = tk.Radiobutton(root, text="Small", variable=option_var, value="Small")
radio2 = tk.Radiobutton(root, text="Medium", variable=option_var, value="Medium")
radio3 = tk.Radiobutton(root, text="Large", variable=option_var, value="Large")

# Pack the radio buttons
radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_choice)
submit_button.pack(pady=10)

# Create a label to display the selected option
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop() 
"""
#3. Payment Method Selection:
""" 
Create a Tkinter application where the user selects a payment method using radio buttons. The available options should be "Credit Card", "Debit Card", and "PayPal". When the user selects an option and clicks the "Proceed" button, display the chosen payment method in a label. 
"""
""" 
import tkinter as tk

def submit_choice():
    # Get the selected option from the radio button group
    selected_option = option_var.get()
    # Update the label to display the selected option
    result_label.config(text=f"Selected Payment Method: {selected_option} ")

# Create the main window
root = tk.Tk()
root.title("Basic Radio Button Selection")
root.geometry("300x200")

# Create a variable to store the selected radio button value
option_var = tk.StringVar()

# Set a default value for the radio buttons
option_var.set("Credit card")

# Create radio buttons
radio1 = tk.Radiobutton(root, text="Credit card", variable=option_var, value="Credit card")
radio2 = tk.Radiobutton(root, text="Debit card", variable=option_var, value="Debit card")
radio3 = tk.Radiobutton(root, text="Paypal", variable=option_var, value="Paypal")

# Pack the radio buttons
radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_choice)
submit_button.pack(pady=10)

# Create a label to display the selected option
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
"""
#6. Multiple Choice Quiz:
""" 
Create a simple quiz application where a question is displayed along with four answer choices as radio buttons. When the user selects an answer and clicks the "Submit" button, check if the answer is correct and display a "Correct" or "Incorrect" message in a label. 
"""
""" 
import tkinter as tk

def check_answer():
    # Get the selected answer from the radio button group
    selected_answer = answer_var.get()
    
    # Check if the selected answer is correct
    if selected_answer == correct_answer:
        result_label.config(text="Correct!", bg="green")
    else:
        result_label.config(text="Incorrect!", bg="red")

# Create the main window
root = tk.Tk()
root.title("Multiple Choice Quiz")
root.geometry("400x300")

# Define the correct answer
correct_answer = "Paris"

# Create a variable to store the selected radio button value
answer_var = tk.StringVar()

# Display the question
question_label = tk.Label(root, text="What is the capital of France?")
question_label.pack(pady=10)

# Create radio buttons for the answer choices
radio1 = tk.Radiobutton(root, text="Berlin", variable=answer_var, value="Berlin")
radio2 = tk.Radiobutton(root, text="Madrid", variable=answer_var, value="Madrid")
radio3 = tk.Radiobutton(root, text="Paris", variable=answer_var, value="Paris")
radio4 = tk.Radiobutton(root, text="Rome", 
variable=answer_var, value="Rome")

# Pack the radio buttons
radio1.pack(pady=5)
radio2.pack(pady=5)
radio3.pack(pady=5)
radio4.pack(pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=10)

# Create a label to display the result (correct/incorrect message)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
"""

