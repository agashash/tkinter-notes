
#1. Number Selection:
""" Create a Tkinter application with a Spinbox widget that allows the user to select a number between 1 and 10. Add a "Submit" button that, when clicked, displays the selected number in a label """

"""
import tkinter as tk

def submit_number():
    # Get the number selected from the spinbox
    selected_number = spinbox.get()
    # Update the label with the selected number
    result_label.config(text=f"You selected: {selected_number}")

# Create the main window
root = tk.Tk()
root.title("Number Selection")
root.geometry("300x200")

# Create a label to instruct the user
instruction_label = tk.Label(root, text="Select a number between 1 and 10:")
instruction_label.pack(pady=10)

# Create a Spinbox for selecting numbers
spinbox = tk.Spinbox(root, from_=1, to=10)
spinbox.pack(pady=5)

# Create a Submit button
submit_button = tk.Button(root, text="Submit", command=submit_number)
submit_button.pack(pady=10)

# Create a label to display the selected number
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
"""
#2. Age Selector:
""" 
Create a form where the user can input their age using a Spinbox widget that ranges from 1 to 100. When the user clicks "Submit", check the age entered and display a message in a label indicating whether the user is a minor (under 18) or an adult (18 and above). 
"""
""" import tkinter as tk

def check_age():
    # Get the age from the spinbox
    age = int(age_spinbox.get())
    
    # Check if the user is a minor or an adult
    if age < 18:
        result_label.config(text="You are a minor.")
    else:
        result_label.config(text="You are an adult.")

# Create the main window
root = tk.Tk()
root.title("Age Selector")
root.geometry("300x200")

# Create a label to instruct the user
instruction_label = tk.Label(root, text="Enter your age:")
instruction_label.pack(pady=10)

# Create a Spinbox for age selection (range 1 to 100)
age_spinbox = tk.Spinbox(root, from_=1, to=100)
age_spinbox.pack(pady=5)

# Create a Submit button
submit_button = tk.Button(root, text="Submit", command=check_age)
submit_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop() """

#3. Time Selector:
"""
Create a Tkinter application that allows the user to select a time using two Spinbox widgets: one for selecting hours (1-12) and one for selecting minutes (0-59). Include a dropdown (Combobox) for AM/PM. When the user clicks "Submit", display the selected time in a label in the format "HH
AM/PM".
"""

""" import tkinter as tk
from tkinter import ttk

def submit_time():
    # Get the selected hour, minute, and AM/PM
    selected_hour = hour_spinbox.get()
    selected_minute = minute_spinbox.get()
    selected_period = am_pm_combobox.get()

    # Format the time and display it in the label
    formatted_time = f"{selected_hour}:{selected_minute} {selected_period}"
    result_label.config(text=f"Selected time: {formatted_time}")

# Create the main window
root = tk.Tk()
root.title("Time Selector")
root.geometry("300x250")

# Create a label to instruct the user
instruction_label = tk.Label(root, text="Select a time:")
instruction_label.pack(pady=10)

# Create a Spinbox for selecting hours (1-12)
hour_spinbox = tk.Spinbox(root, from_=1, to=12, width=5)
hour_spinbox.pack(pady=5)

# Create a Spinbox for selecting minutes (0-59)
minute_spinbox = tk.Spinbox(root, from_=0, to=59, width=5)
minute_spinbox.pack(pady=5)

# Create a Combobox for selecting AM/PM
am_pm_combobox = ttk.Combobox(root, values=["AM", "PM"], width=5)
am_pm_combobox.set("AM")  # Default value
am_pm_combobox.pack(pady=5)

# Create a Submit button
submit_button = tk.Button(root, text="Submit", command=submit_time)
submit_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
"""

#4. Temperature Converter:
""" 
Create a Tkinter application that allows the user to input a temperature using a Spinbox. The range should be from -50 to 50 degrees Celsius. Add a button that, when clicked, converts the Celsius value to Fahrenheit and displays the result in a label. 
"""
""" 
import tkinter as tk

def convert_temperature():
    # Get the Celsius value from the spinbox
    celsius = float(temp_spinbox.get())
    
    # Convert Celsius to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    
    # Display the result in the result_label
    result_label.config(text=f"{celsius}°C is {fahrenheit:.2f}°F")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

# Create a label to instruct the user
instruction_label = tk.Label(root, text="Enter temperature in Celsius:")
instruction_label.pack(pady=10)

# Create a Spinbox for selecting temperature (range -50 to 50 degrees Celsius)
temp_spinbox = tk.Spinbox(root, from_=-50, to=50, width=10)
temp_spinbox.pack(pady=5)

# Create a Convert button
convert_button = tk.Button(root, text="Convert to Fahrenheit", command=convert_temperature)
convert_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop() 
"""


#5. Quantity Selector for an Order:
""" 
Create a product ordering form where the user can select a quantity for a product using a Spinbox that ranges from 1 to 50. Add a "Submit Order" button that, when clicked, displays the total cost based on the selected quantity (e.g., $10 per product) in a label. 
"""
"""
import tkinter as tk

def submit_order():
    # Get the quantity from the Spinbox
    quantity = int(quantity_spinbox.get())
    
    # Define the price per product
    price_per_product = 10.00  # $10 per product
    
    # Calculate the total cost
    total_cost = quantity * price_per_product
    
    # Display the total cost in the result_label
    result_label.config(text=f"Total cost: ${total_cost:.2f}")

# Create the main window
root = tk.Tk()
root.title("Product Order Form")
root.geometry("300x200")

# Create a label to instruct the user
instruction_label = tk.Label(root, text="Select quantity (1-50):")
instruction_label.pack(pady=10)

# Create a Spinbox for selecting quantity (range 1 to 50)
quantity_spinbox = tk.Spinbox(root, from_=1, to=50, width=5)
quantity_spinbox.pack(pady=5)

# Create a Submit Order button
submit_button = tk.Button(root, text="Submit Order", command=submit_order)
submit_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
"""