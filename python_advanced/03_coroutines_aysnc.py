# 📌 Asynchronous Programming in Python with asyncio

# ✅ What is Asynchronous Programming?
# Asynchronous programming allows the program to perform non-blocking operations, 
# meaning the program can execute other tasks while waiting for long-running operations (like network calls or IO).

import asyncio

# Define an asynchronous function
async def say_hello():
    await asyncio.sleep(1)  # Simulate a non-blocking operation
    print("Hello!")  # This message is printed after 1 second

# Run the asynchronous function using asyncio.run()
asyncio.run(say_hello())

# Output:
# Hello! (printed after 1 second delay)
