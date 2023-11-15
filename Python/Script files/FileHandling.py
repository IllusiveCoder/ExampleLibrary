# Example 2: Reading and writing to a file

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text.")

# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()

# Output the content
print("File Content:", content)
