class Vehicle:
    def __init__(self, mark,model):
        self.mark = mark
        self.model = model
    
    def fuel_type(self):
        return "Unknown"

    def passenger_capacity(self):
        return 0
        
class Car(Vehicle):
    def fuel_type(self):
        return "Gasoline" or self.fuel == "Alcohol"
        
    def passenger_capacity(self):
        return 5

class Motorcycle(Vehicle):
    def fuel_type(self):
        return "Gasoline"
            
    def passenger_capacity(self):
        return 2

class Truck(Vehicle):
    def fuel_type(self):
        return "Diesel"
    
    def passenger_capacity(self):
        return 2
