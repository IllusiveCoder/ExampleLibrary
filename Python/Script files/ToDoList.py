# Simple To-Do List

'''This program implements a basic to-do list application. 
Users can add tasks, view the list, and mark tasks as completed 
or remove them. 
It demonstrates the use of lists and basic user interaction.'''

# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to view all tasks
def view_tasks():
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

# Function to mark a task as completed
def complete_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print("Completed task:", completed_task)
    else:
        print("Invalid task index.")

# Usage
while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_index = int(input("Enter task index to complete: "))
        complete_task(task_index)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
