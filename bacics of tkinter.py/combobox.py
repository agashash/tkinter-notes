#1. Basic Combobox Selection:
""" 
Create a Tkinter application with a Combobox that contains a list of three colors: Red, Green, and Blue. When the user selects a color and clicks a button, display a label that shows the selected color. 
"""
""" 
import tkinter as tk
from tkinter import ttk

def show_color():
    # Get the selected color from the combobox
    selected_color = color_combobox.get()
    
    # Display the selected color in the result label
    result_label.config(text=f"Selected Color: {selected_color}")

# Create the main window
root = tk.Tk()
root.title("Color Selector")
root.geometry("300x200")

# Create a label to instruct the user
instruction_label = tk.Label(root, text="Select a color:")
instruction_label.pack(pady=10)

# Create a combobox with three color options
color_combobox = ttk.Combobox(root, values=["Red", "Green", "Blue"], state="readonly")
color_combobox.pack(pady=5)

# Create a button to display the selected color
select_button = tk.Button(root, text="Show Color", command=show_color)
select_button.pack(pady=10)

# Create a label to display the selected color
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop() 
"""

#2. Dynamic Label Update:
""" 
Create a Tkinter application with a Combobox containing a list of three programming languages: Python, Java, and C++. When the user selects a programming language, immediately update a label to display a message like "You selected: [Language]".

"""
""" 
import tkinter as tk
from tkinter import ttk

def update_label(event):
    # Get the selected programming language
    selected_language = language_combobox.get()
    
    # Update the label to display the selected language
    result_label.config(text=f"You selected: {selected_language}")

# Create the main window
root = tk.Tk()
root.title("Programming Language Selector")
root.geometry("300x200")

# Create a label to instruct the user
instruction_label = tk.Label(root, text="Select a programming language:")
instruction_label.pack(pady=10)

# Create a combobox with three programming language options
language_combobox = ttk.Combobox(root, values=["Python", "Java", "C++"], state="readonly")
language_combobox.pack(pady=5)

# Bind the combobox selection event to update the label
language_combobox.bind("<<ComboboxSelected>>", update_label)

# Create a label to display the selected programming language
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
"""

#3. Combobox with Cities:
""" 
Create a form where the user can select a city from a Combobox. After selecting the city and clicking a "Submit" button, display a label saying "You selected [city name]". The cities in the Combobox should include New York, London, and Tokyo. 
"""
""" import tkinter as tk
from tkinter import ttk

def submit_city():
    # Get the selected city from the combobox
    selected_city = city_combobox.get()
    
    # Update the result label to display the selected city
    result_label.config(text=f"You selected: {selected_city}")

# Create the main window
root = tk.Tk()
root.title("City Selector")
root.geometry("300x200")

# Create a label to instruct the user
instruction_label = tk.Label(root, text="Select a city:")
instruction_label.pack(pady=10)

# Create a combobox with city options
city_combobox = ttk.Combobox(root, values=["New York", "London", "Tokyo"], state="readonly")
city_combobox.pack(pady=5)

# Create a submit button to display the selected city
submit_button = tk.Button(root, text="Submit", command=submit_city)
submit_button.pack(pady=10)

# Create a label to display the selected city
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
"""

