# Lesson 8: File Handling in Python

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("This is the second line.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)
