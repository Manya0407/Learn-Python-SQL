# 📌 List Comprehensions in Python

# ✅ Basic Syntax:
# [expression for item in iterable if condition]

# Example 1: Create a list of squares for numbers 1 to 5
squares = [x ** 2 for x in range(1, 6)]
print("🔹 Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# Example 2: Get even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print("🔹 Even Numbers:", even_numbers)  # Output: [0, 2, 4, 6, 8]

# Example 3: Convert list of words to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print("🔹 Uppercase Words:", uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Example 4: Create a list of tuples (number, square)
number_square_pairs = [(x, x ** 2) for x in range(1, 6)]
print("🔹 Number-Square Pairs:", number_square_pairs)  
# Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Example 5: Flatten a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened_list = [num for sublist in nested_list for num in sublist]
print("🔹 Flattened List:", flattened_list)  # Output: [1, 2

