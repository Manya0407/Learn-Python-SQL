# 📌 Custom Exception Class in Python

# ✅ What is a Custom Exception?
# Custom exceptions allow you to define your own error types that can be raised and caught in your program.

# Define a custom exception
class CustomError(Exception):
    pass  # You can customize the error message or add functionality here

# Raise and catch the custom exception
try:
    raise CustomError("This is a custom exception!")
except CustomError as e:
    print(e)  # Output the exception message

# Output:
# This is a custom exception!
