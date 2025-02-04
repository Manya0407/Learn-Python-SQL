# 📌 Context Manager with `with` Statement

# ✅ What is a Context Manager?
# A context manager is an object that defines the runtime context to be established when the code within a `with` block is executed.
# It ensures that certain actions are performed before and after the code within the `with` block is executed (e.g., opening/closing files).

class FileManager:
    def __init__(self, filename, mode):
        self.file = open(filename, mode)  # Open the file when the object is created

    def __enter__(self):
        # This method is called when the `with` block is entered
        return self.file  # Return the file object to be used in the block

    def __exit__(self, exc_type, exc_val, exc_tb):
        # This method is called when the `with` block is exited
        self.file.close()  # Close the file when the block ends

# Using the context manager to write to a file
with FileManager("test.txt", "w") as file:
    file.write("Hello, World!")  # This block writes to the file

# Output:
# The file "test.txt" is created and contains the text "Hello, World!".
