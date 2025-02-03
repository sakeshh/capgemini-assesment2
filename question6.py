# 6. Implement a multi-level inheritance example where `Vehicle` is a base class,
#  `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.

class Vechicle:
    def __init__(self,type):
        self.type=type
    def show(self):
        print(f"vechile is {self.type}")
class Car(Vechicle):
    def __init__(self, type,seats,tyres):
        super().__init__(type)
        self.seats=seats
        self.tyres=tyres
    def car_details(self):
        print(f"car consists of {self.seats} seats ,tyres: {self.tyres} and {self.type} vechile")
class Bike(Vechicle):
    def __init__(self, type,model,mileage):
        super().__init__(type)
        self.model=model
        self.mileage=mileage
    def bike_details(self):
        print(f"bike is {self.type} ,model is {self.model} and mileage is {self.mileage}")
class Electric_car(Car):
    def __init__(self, type, seats, tyres,range):
        super().__init__(type, seats, tyres)
        self.range=range
    def electric_car_details(self):
        print(f"electric car is {self.type}, tyres:{self.tyres},seats:{self.seats} and its range is:{self.range}")
electric=Electric_car("geared","4","5",120)
electric.electric_car_details()
electric.car_details()
electric.show()
bike=Bike("geared","fz",45)
bike.bike_details()