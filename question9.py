# 9. Simulate multiple inheritance where `FlyingCar` inherits from 
# both `Car` and `Airplane`. Handle potential conflicts in the `move()` method.

class Car:
    def move(self):
        print("this method is for car")
class Airplane:
    def move(self):
        print("this method is for airplane")
class FlyingCar(Car,Airplane):
    def move(self):
        print("this method is flyingcar")
        Car.move(self)
        print()
        Airplane.move(self)
fly=FlyingCar()
fly.move()


