# A class representing a user
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

# A list to store the users
users = []

# Function to add a user
def add_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User(username, password)
    users.append(user)
    print("User", username, "successfully added.")

# Function to check login credentials
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users:
        if user.username == username and user.check_password(password):
            print("Login successful. Welcome,", username)
            return
    print("Invalid username or password.")

# Main program
while True:
    print("1. Add User")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_user()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")