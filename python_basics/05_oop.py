# Lesson 5: Object-Oriented Programming (OOP) in Python

# Define a simple class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Create an object (instance) of the class
student1 = Student("Alice", 22)

# Call the method
print(student1.introduce())
