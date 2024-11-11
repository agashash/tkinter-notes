#1. Basic Checkbox Selection:
""" 
Create a Tkinter application with two checkboxes labeled "I agree to the Terms and Conditions" and "Subscribe to Newsletter." When the user clicks a submit button, display a message in a label indicating which options were selected. 
"""

"""
 import tkinter as tk


def check():
    sub=res_sub.get()
    like=res_like.get()

    message="you selected"

    if sub:
        message += "\n subscribe our chaneel"
    if like:
        message += "\n like our chaneel"
    if not sub and not like:
        message+="\n you selected nothing"
        
    label.config(text=message)


root=tk.Tk()
root.title("checkbutton")
root.geometry("600x400")

res_sub=tk.IntVar()
res_like=tk.IntVar()

check1=tk.Checkbutton(root,text="subscribe our chaneel", variable=res_sub).place(x=250,y=50)
check2=tk.Checkbutton(root,text="like our channel", variable=res_like).place(x=250,y=100)
button=tk.Button(root,text="submit",command=check).place(x=300,y=150)
label=tk.Label(root,text="")
label.pack(padx=60,pady=80)
root.mainloop()
"""

#2. Multiple Selection:

""" 
Create a Tkinter form with three checkboxes: "Python", "Java", and "C++". When the user clicks a submit button, display the selected programming languages in a label. If no checkboxes are selected, display a message saying "No languages selected."
"""

""" 
import tkinter as tk


def check():
    java1=res_java.get()
    python1=res_python.get()
    c1=res_c
    message="you selected"

    if java1:
        message += "\n java"
    if python1:
        message += "\n python"
    if c1:
        message += "\n c++"    
    if not java1 and not python1 and not c1:
        message+="\n no language selected"
        
    label.config(text=message)


root=tk.Tk()
root.title("checkbutton")
root.geometry("600x400")
root.config(bg="lightblue")

res_java=tk.IntVar()
res_python=tk.IntVar()
res_c=tk.IntVar()

check1=tk.Checkbutton(root,text="java", variable=res_java,bg="lightgreen").place(x=250,y=50)
check2=tk.Checkbutton(root,text=" python", variable=res_python,bg="lightgreen").place(x=250,y=100)
check3=tk.Checkbutton(root,text="c++", variable=res_c,bg="lightgreen").place(x=250,y=150)


button=tk.Button(root,text="submit",bg="red",command=check).place(x=300,y=200)
label=tk.Label(root,text="",bg="lightblue",fg="brown")
label.place(x=290,y=250)
root.mainloop()
"""

#3. Enable/Disable Button with Checkbox:
'''
Create a Tkinter application where a button is initially disabled. Include a checkbox labeled "I accept the terms". When the user checks the checkbox, enable the button. If the checkbox is unchecked, disable the button again.
'''
""" 
import tkinter as tk

def toggle_button():
    # Check if the checkbox is checked (value = 1)
    if terms_var.get() == 1:
        submit_button.config(state="normal")  # Enable the button
    else:
        submit_button.config(state="disabled")  # Disable the button

# Create the main window
root = tk.Tk()
root.title("Enable/Disable Button")
root.geometry("300x200")

# Variable to track the state of the checkbox
terms_var = tk.IntVar()

# Create the checkbox with the label "I accept the terms"
terms_checkbox = tk.Checkbutton(root, text="I accept the terms", variable=terms_var, command=toggle_button)
terms_checkbox.pack(pady=10)

# Create a button that is initially disabled
submit_button = tk.Button(root, text="Submit", state="disabled")
submit_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop() 
"""

#4. Mandatory Checkbox:

""" 
Create a form where the user has to agree to the Terms and Conditions by checking a checkbox before submitting the form. If the checkbox is not selected and the user clicks the submit button, display an error message saying "You must agree to the Terms and Conditions."
"""
"""
import tkinter as tk

def submit_form():
    # Check if the checkbox is checked (value = 1)
    if terms_var.get() == 1:
        result_label.config(text="Form Submitted!", fg="green")
    else:
        result_label.config(text="You must agree to the Terms and Conditions.", fg="red")

# Create the main window
root = tk.Tk()
root.title("Mandatory Checkbox Example")
root.geometry("300x200")

# Variable to track the state of the checkbox
terms_var = tk.IntVar()

# Create the checkbox with the label "I agree to the Terms and Conditions"
terms_checkbox = tk.Checkbutton(root, text="I agree to the Terms and Conditions", variable=terms_var)
terms_checkbox.pack(pady=10)

# Create a submit button that calls the submit_form function
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Create a label to display the result (error or success message)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

"""

#7. Multiple Comboboxes for Date:

""" 
Create a Tkinter application that lets the user select a date using three Combobox widgets: one for the day (1-31), one for the month (January to December), and one for the year (2020-2024). When the user clicks a "Submit" button, display the selected date in the format "DD Month YYYY" in a label. 
"""
""" 
import tkinter as tk
from tkinter import ttk

def submit_date():
    # Get the selected values from the Comboboxes
    day = day_combobox.get()
    month = month_combobox.get()
    year = year_combobox.get()

    # If any field is not selected, display an error message
    if not day or not month or not year:
        result_label.config(text="Please select a valid date.", fg="red")
    else:
        # Display the selected date in the label
        result_label.config(text=f"Selected Date: {day} {month} {year}", fg="green")

# Create the main window
root = tk.Tk()
root.title("Date Selector")
root.geometry("350x275")

# Create a list of days (1-31)
days = [str(i) for i in range(1, 32)]

# Create a list of months (January to December)
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# Create a list of years (2020-2024)
years = [str(i) for i in range(2020, 2025)]

# Day Combobox
day_label = tk.Label(root, text="Day:")
day_label.pack(pady=5)
day_combobox = ttk.Combobox(root, values=days)
day_combobox.pack(pady=5)

# Month Combobox
month_label = tk.Label(root, text="Month:")
month_label.pack(pady=5)
month_combobox = ttk.Combobox(root, values=months)
month_combobox.pack(pady=5)

# Year Combobox
year_label = tk.Label(root, text="Year:")
year_label.pack(pady=5)
year_combobox = ttk.Combobox(root, values=years)
year_combobox.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_date)
submit_button.pack(pady=10)

# Result Label to display the selected date
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
"""