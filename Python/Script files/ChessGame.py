# Chess Game
# A simple text-based chess game for two players.

'''Description: This program implements a simple text-based chess 
game where two players can take turns making moves on the board.'''

# Initialize the chessboard as a 2D list
chessboard = [["R", "N", "B", "Q", "K", "B", "N", "R"],
              ["P", "P", "P", "P", "P", "P", "P", "P"],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " ", " ", " "],
              ["p", "p", "p", "p", "p", "p", "p", "p"],
              ["r", "n", "b", "q", "k", "b", "n", "r"]]

# Print the initial chessboard
for row in chessboard:
    print(" ".join(row))

# Main game loop
while True:
    move = input("Enter your move (e.g., 'e2 e4'): ")
    from_col, from_row, to_col, to_row = move.split()
    from_col = ord(from_col) - ord("a")
    from_row = 8 - int(from_row)
    to_col = ord(to_col) - ord("a")
    to_row = 8 - int(to_row)

    # Move the piece
    chessboard[to_row][to_col] = chessboard[from_row][from_col]
    chessboard[from_row][from_col] = " "

    # Print the updated chessboard
    for row in chessboard:
        print(" ".join(row))
