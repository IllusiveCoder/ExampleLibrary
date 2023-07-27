import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, date, category, amount):
        if date not in self.expenses:
            self.expenses[date] = []
        self.expenses[date].append({"category": category, "amount": amount})

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.expenses, file)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            pass

    def get_daily_summary(self, date):
        total = 0
        if date in self.expenses:
            for expense in self.expenses[date]:
                total += expense["amount"]
        return total

# Usage example
tracker = ExpenseTracker()
tracker.add_expense("2023-07-19", "Groceries", 50)
tracker.add_expense("2023-07-19", "Transportation", 30)
tracker.add_expense("2023-07-20", "Dining", 25)
tracker.save_to_file("expenses.json")

# Load the expenses from the file and get the daily summary
tracker.load_from_file("expenses.json")
print("Total expenses on 2023-07-19:", tracker.get_daily_summary("2023-07-19"))
