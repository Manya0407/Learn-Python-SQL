# 📌 Mini-Project: Vehicle Management System
# 🎯 Goal: Implement inheritance for different vehicle types

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

# 🚗 Car (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def info(self):
        return f"{self.brand} {self.model} with {self.doors} doors 🚗"

# 🏍️ Bike (inherits from Vehicle)
class Bike(Vehicle):
    def __init__(self, brand, model, type_of_bike):
        super().__init__(brand, model)
        self.type_of_bike = type_of_bike

    def info(self):
        return f"{self.brand} {self.model} - {self.type_of_bike} 🏍️"

# ✅ Creating Vehicles
car1 = Car("Toyota", "Camry", 4)
bike1 = Bike("Honda", "CBR", "Sport Bike")

print(car1.info())
print(bike1.info())

# Output:
# Toyota Camry with 4 doors 🚗
# Honda CBR - Sport Bike 🏍️
