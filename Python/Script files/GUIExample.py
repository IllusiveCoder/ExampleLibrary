# Example: GUI Application - Simple To-Do List

'''
Explanation:
    This program creates a simple to-do list using the tkinter library for the graphical user interface.
    Users can add tasks using the entry field, and tasks can be deleted by selecting and clicking the "Delete Task" button.
'''

import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# GUI setup
root = tk.Tk()
root.title("To-Do List")

# Entry for new tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=40)
listbox.pack()

# Buttons for adding and deleting tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Start the GUI
root.mainloop()
