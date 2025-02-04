# 📌 Inheritance in Python (Reusing Code)

# ✅ What is Inheritance?
# Inheritance allows a **child class** to use methods and attributes from a **parent class**.

# Example: Parent Class (Animal)
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

# Child Class (Dog) - Inherits from Animal
class Dog(Animal):
    def speak(self):
        return "Bark! 🐶"

# Child Class (Cat) - Inherits from Animal
class Cat(Animal):
    def speak(self):
        return "Meow! 🐱"

# Creating Objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name, "says:", dog.speak())  # Output: Buddy says: Bark! 🐶
print(cat.name, "says:", cat.speak())  # Output: Whiskers says: Meow! 🐱

# ✅ Why Use Inheritance?
# 1️⃣ Reduces code duplication  
# 2️⃣ Allows extending functionality easily  
# 3️⃣ Supports **super()** to call parent methods  
