import random
import string

'''The Random Password Generator generates random 
strong passwords of a specified length. The passwords 
include a mix of uppercase letters, lowercase letters, 
numbers, and special characters. Users can specify 
the desired password length, and the program will 
create and display the generated password.'''

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example
generated_password = generate_password()
print("Generated Password:", generated_password)

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True