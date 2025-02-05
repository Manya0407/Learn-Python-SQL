# 📌 File Handling in Python

# ✅ Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, world!\n")

# ✅ Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# ✅ Appending to a file
with open("sample.txt", "a") as file:
    file.write("Appending a new line.\n")
