#1. Basic ScrolledText Widget:
"""
 Create a Tkinter application with a ScrolledText widget where the user can type in a block of text. Add a "Clear Text" button that, when clicked, clears all the text from the ScrolledText widget. 
"""
"""
import tkinter as tk
from tkinter import scrolledtext

def clear_text():
    # Clear all the text from the ScrolledText widget
    text_area.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("ScrolledText Example")
root.geometry("400x300")

# Create a ScrolledText widget
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(pady=10)

# Create a button to clear the text
clear_button = tk.Button(root, text="Clear Text", command=clear_text)
clear_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
"""
#2. Word Counter:
""" 
Create a Tkinter application with a ScrolledText widget where the user can enter multiple lines of text. Add a "Count Words" button that, when clicked, counts and displays the total number of words in the text. 
"""
""" 
import tkinter as tk
from tkinter import scrolledtext

def count_words():
    # Get the content from the ScrolledText widget
    text_content = text_area.get(1.0, tk.END)
    
    # Split the content into words
    words = text_content.split()
    
    # Count the number of words
    word_count = len(words)
    
    # Display the word count in the result label
    result_label.config(text=f"Word Count: {word_count}")

# Create the main window
root = tk.Tk()
root.title("Word Counter")
root.geometry("400x300")

# Create a ScrolledText widget
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(pady=10)

# Create a button to count the words
count_button = tk.Button(root, text="Count Words", command=count_words)
count_button.pack(pady=10)

# Create a label to display the word count result
result_label = tk.Label(root, text="Word Count: 0")
result_label.pack(pady=10) 

# Run the Tkinter main loop
root.mainloop()
"""
#3. Note Taking Application:
""" 
Create a simple note-taking application using a ScrolledText widget. Add a "Save" button that, when clicked, saves the contents of the ScrolledText to a text file. Also, add a "Load" button that loads the text from the file back into the ScrolledText widget.
"""

""" 
 import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

def save_note():
    # Get the content from the ScrolledText widget
    note_content = text_area.get(1.0, tk.END)
    
    # Open a file dialog to save the text file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    
    # If the user provides a file path, save the content to the file
    if file_path:
        with open(file_path, 'w') as file:
            file.write(note_content)

def load_note():
    # Open a file dialog to load a text file
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    
    # If a file is selected, read the content and insert it into the ScrolledText widget
    if file_path:
        with open(file_path, 'r') as file:
            note_content = file.read()
            text_area.delete(1.0, tk.END)  # Clear the current text
            text_area.insert(tk.INSERT, note_content)  # Insert the loaded content

# Create the main window
root = tk.Tk()
root.title("Note Taking Application")
root.geometry("500x400")

# Create a ScrolledText widget
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15)
text_area.pack(pady=10)

# Create a Save button
save_button = tk.Button(root, text="Save", command=save_note)
save_button.pack(pady=5)

# Create a Load button
load_button = tk.Button(root, text="Load", command=load_note)
load_button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
"""
