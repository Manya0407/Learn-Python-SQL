# 📌 Error Handling in Python (try-except-finally)

# ✅ What is Error Handling?
# Error handling lets you catch exceptions and handle them gracefully.

try:
    x = int(input("Enter a number: "))  # May cause ValueError
    result = 10 / x  # May cause ZeroDivisionError
    print("Result:", result)
except ValueError:
    print("❌ Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("❌ Error: Division by zero is not allowed.")
finally:
    print("✅ Program execution completed.")
