# 📌 Decorators in Python (Modify Functions Without Changing Them)

# ✅ What is a Decorator?
# A decorator is a function that takes another function as input and **modifies its behavior**.

# ✅ Syntax:
# def decorator_function(original_function):
#     def wrapper_function():
#         # Modify behavior
#         original_function()
#     return wrapper_function

# Example: Simple Decorator
def decorator(func):
    def wrapper():
        print("✨ Before function call")
        func()
        print("✨ After function call")
    return wrapper

@decorator  # Applying the decorator
def say_hello():
    print("Hello, world! 🌍")

say_hello()

# Output:
# ✨ Before function call
# Hello, world! 🌍
# ✨ After function call

# ✅ Why Use Decorators?
# 1️⃣ Add functionality to functions dynamically  
# 2️⃣ Used for **logging, authentication, caching**  
# 3️⃣ Helps write **cleaner & reusable** code  
