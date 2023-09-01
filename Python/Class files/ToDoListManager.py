# To-Do List Manager class

'''Description: This program allows users to manage a to-do list. 
Users can add tasks, mark tasks as completed, and view their to-do 
list.'''

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] += " (Completed)"

    def view_list(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

# Example usage
todo_list = ToDoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Read a book")
todo_list.view_list()
todo_list.mark_task_completed(0)
todo_list.view_list()
