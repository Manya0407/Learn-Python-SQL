# 📌 Mini-Project: Employee Manager System
# 🎯 Goal: Use OOP to create Employee objects with unique IDs

class Employee:
    emp_count = 0  # Class attribute to track employee count

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1
        self.emp_id = Employee.emp_count  # Unique ID for each employee

    def display_info(self):
        return f"🆔 {self.emp_id} | {self.name} | 💰 ${self.salary}"

# ✅ Creating Employees
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.display_info())
print(emp2.display_info())

# Output:
# 🆔 1 | Alice | 💰 $50000
# 🆔 2 | Bob | 💰 $60000
