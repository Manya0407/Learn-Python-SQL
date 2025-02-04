# 📌 Lambda Functions in Python (Anonymous Functions)

# ✅ What is a Lambda Function?
# A lambda function is a small **anonymous function** (i.e., without a name).
# It can have any number of arguments but **only one expression**.

# ✅ Basic Syntax:
# lambda arguments: expression

# Example 1: Square of a number
square = lambda x: x ** 2
print("🔹 Square of 4:", square(4))  # Output: 16

# Example 2: Add two numbers
add = lambda a, b: a + b
print("🔹 Sum of 3 and 7:", add(3, 7))  # Output: 10

# Example 3: Find maximum of two numbers
maximum = lambda x, y: x if x > y else y
print("🔹 Maximum of (5, 8):", maximum(5, 8))  # Output: 8

# Example 4: Use in list sorting (Sort names by length)
names = ["Alice", "Bob", "Charlotte", "David"]
names.sort(key=lambda name: len(name))  # Sorting by name length
print("🔹 Sorted Names by Length:", names)  # Output: ['Bob', 'Alice', 'David', 'Charlotte']

# Example 5: Use with filter() to get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("🔹 Even Numbers:", even_numbers)  # Output: [2, 4, 6, 8]

# Example 6: Use with map() to double numbers
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("🔹 Doubled Numbers:", doubled_numbers)  # Output: [2, 4, 6, 8, 10, 12, 14, 16]

# Example 7: Use with reduce() to find the sum of numbers
from functools import reduce
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("🔹 Sum of Numbers:", sum_of_numbers)  # Output: 36

# ✅ Key Advantages of Lambda Functions:
# 1️⃣ Concise and compact (no need for defining functions explicitly)
# 2️⃣ Useful in functions like **map(), filter(), and reduce()**
# 3️⃣ Improves code readability for small operations

