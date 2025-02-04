# 📌 JSON Handling in Python (Working with JSON Data)

# ✅ What is JSON?
# JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write.
# It's commonly used for exchanging data between a client and a server, or for storing data in a structured format.

# ✅ Python's json Module
# Python provides the built-in `json` module to work with JSON data. It can be used to:
# 1️⃣ Convert Python objects into JSON strings (`json.dumps()`).
# 2️⃣ Parse JSON strings into Python objects (`json.loads()`).

# Example: Converting Python Dictionary to JSON String

import json

# A Python dictionary with sample data
data = {"name": "Alice", "age": 25}

# Converting Python dictionary to a JSON string using json.dumps()
# This will serialize the Python object into a JSON-formatted string
json_data = json.dumps(data)

# Print the resulting JSON string
print("JSON Data:", json_data)

# Output:
# JSON Data: {"name": "Alice", "age": 25}

# ✅ Why Use JSON in Python?
# JSON is widely used for data exchange because it is:
# 1️⃣ **Human-readable**: Easy to read and write.
# 2️⃣ **Language-independent**: JSON can be used across many programming languages.
# 3️⃣ **Lightweight**: Efficient for sending and receiving data over networks.

# ✅ Common JSON Operations:
# - **json.dumps()**: Serialize a Python object to a JSON string.
# - **json.loads()**: Deserialize a JSON string into a Python object.

# Example: Converting JSON Back to Python (Deserialization)
json_string = '{"name": "Bob", "age": 30}'

# Convert the JSON string back into a Python dictionary using json.loads()
python_data = json.loads(json_string)

# Print the Python dictionary
print("Python Data:", python_data)

# Output:
# Python Data: {'name': 'Bob', 'age': 30}
