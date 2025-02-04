# 📌 Decorators in Python (Modify Functions Without Changing Them)

# ✅ What is a Decorator?
# A decorator is a function that takes another function as input and **modifies its behavior** without changing the actual function code.

# ✅ Syntax:
# Decorators are defined with the following structure:
# 1. A decorator function that accepts the original function as an argument.
# 2. A wrapper function inside the decorator that modifies the behavior of the original function.
# 3. The wrapper function returns the modified behavior.

# Example: Simple Decorator
def decorator(func):
    # Wrapper function inside the decorator
    def wrapper():
        print("✨ Before function call")  # Pre-execution behavior
        func()  # Call the original function
        print("✨ After function call")  # Post-execution behavior
    return wrapper

# Applying the decorator to a function using the '@' symbol
@decorator
def say_hello():
    print("Hello, world! 🌍")

# Calling the decorated function
say_hello()

# Output:
# ✨ Before function call
# Hello, world! 🌍
# ✨ After function call

# ✅ Why Use Decorators?
# 1️⃣ **Add functionality to functions dynamically**:
#    - Decorators allow you to extend or modify the behavior of functions without changing their code. For example, you can add logging, performance monitoring, or validation checks easily.
# 2️⃣ **Common Use Cases**:
#    - **Logging**: Automatically log the execution of functions.
#    - **Authentication**: Check if a user is authenticated before calling a function.
#    - **Caching**: Cache the results of expensive function calls.
# 3️⃣ **Write cleaner & reusable code**:
#    - Decorators allow you to abstract repetitive functionality into reusable components, leading to more readable and maintainable code.

# Let's look at more examples of decorators in action!

# Example 1: Logging Decorator
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} was called with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call  # Apply the logging decorator
def add(a, b):
    return a + b

# Calling the decorated add function
result = add(3, 4)
print(f"Result: {result}")

# Output:
# Function add was called with arguments (3, 4) and keyword arguments {}
# Result: 7

# Example 2: Caching Results with a Decorator
def cache_results(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Fetching cached result for {args}")
            return cache[args]
        else:
            print(f"Calculating result for {args}")
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@cache_results  # Apply the caching decorator
def expensive_computation(x):
    return x * x  # Simulate a time-consuming computation

# First call (no cache)
print(expensive_computation(5))  # Output: Calculating result for (5)

# Second call (cache hit)
print(expensive_computation(5))  # Output: Fetching cached result for (5)
