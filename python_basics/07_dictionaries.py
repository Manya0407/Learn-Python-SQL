# Lesson 7: Dictionaries in Python

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A"
}

# Accessing values
print("Student Name:", student["name"])

# Adding a new key-value pair
student["course"] = "Computer Science"

# Iterating over dictionary keys and values
for key, value in student.items():
    print(f"{key}: {value}")
