# Love Letter Generator
# A program that generates a love letter based on user input.

'''Description: This program generates a love letter by asking the 
user's name and their feelings for a special someone.'''

# Get user input
sender_name = input("Enter your name: ")
recipient_name = input("Enter the recipient's name: ")
feelings = input("Write a sentence about your feelings: ")

# Generate the love letter
love_letter = f"Dear {recipient_name},\n\nI hope this message finds you well. I wanted to take a moment to express my feelings towards you. {feelings} Every moment I spend with you is a cherished memory that I hold close to my heart.\n\nYou bring immense joy and happiness into my life, and I am truly grateful for your presence. Your smile lights up my world, and your kindness and warmth never cease to amaze me.\n\nWith all my love,\n{sender_name}"

# Print the love letter
print("\nHere is your love letter:\n")
print(love_letter)
