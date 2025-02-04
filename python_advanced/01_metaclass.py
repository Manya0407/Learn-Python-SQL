# 📌 Metaclass Example in Python

# ✅ What is a Metaclass?
# A metaclass in Python is a class for classes. It defines how a class behaves. 
# You can use metaclasses to modify or customize the creation and behavior of classes.

# ✅ How does a Metaclass work?
# When you define a class, Python uses the metaclass to create the class. 
# By overriding the `__new__` or `__init__` methods in the metaclass, 
# you can customize the behavior of class creation.

class Meta(type):
    # The `__new__` method is called when the class is being created.
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")  # Print a message when the class is being created
        return super().__new__(cls, name, bases, dct)  # Call the parent class to create the class

# Creating a class `MyClass` with the metaclass `Meta`
class MyClass(metaclass=Meta):
    pass

# Output:
# Creating class MyClass
