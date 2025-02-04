# 📌 Generators in Python (Memory-Efficient Iterators)

# ✅ What is a Generator?
# A generator function **yields** values one by one instead of returning all at once.
# This makes it **memory efficient** for large datasets.

# ✅ Syntax:
# def generator():
#     yield value

# Example: Countdown Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the Generator
for num in countdown(5):
    print(num)

# Output: 
# 5
# 4
# 3
# 2
# 1

# ✅ Why Use Generators?
# 1️⃣ Saves memory (doesn't store all values at once)
# 2️⃣ Supports **lazy evaluation** (computes values only when needed)
# 3️⃣ Used in **big data processing** and **streaming APIs**
