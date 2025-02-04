# 📌 Object-Oriented Programming (OOP) - Classes in Python

# ✅ What is OOP?
# OOP (Object-Oriented Programming) is a way of structuring code using **classes** and **objects**.

# ✅ Class Syntax:
# class ClassName:
#     def __init__(self, parameters):
#         self.attribute = parameter
#     def method(self):
#         return something

# Example: Define a `Car` class
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute 1
        self.model = model  # Attribute 2

    def display_info(self):
        return f"🚗 Car: {self.brand} {self.model}"

# Creating an object (instance) of the class
car1 = Car("Toyota", "Corolla")
print(car1.display_info())  # Output: 🚗 Car: Toyota Corolla

# ✅ Key OOP Features:
# 1️⃣ **Encapsulation** - Data is wrapped inside objects.
# 2️⃣ **Abstraction** - Hides unnecessary details.
# 3️⃣ **Inheritance** - One class can inherit from another.
# 4️⃣ **Polymorphism** - Different classes can have methods with the same name.
