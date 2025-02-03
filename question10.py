# 10. Build a `SmartPhone` class inheriting from `MobileDevice`, 
# which in turn inherits from `Electronics`. Demonstrate method overriding 
# and attribute reuse.

class Electronics:
    def __init__(self,brand):
        self.brand=brand
        
    def show(self):
        print(f"brand is {self.brand}")
class MobileDevices(Electronics):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
    def show(self):
        Electronics.show(self)
        print(f"Mobile is {self.model}")
class Smartphone(MobileDevices):
    def __init__(self, brand,model,price):
        super().__init__(brand,model)
        self.price=price
    def show(self):
        MobileDevices.show(self)
        print(f"model is {self.model},brand:{self.brand},price:{self.price}")
        
smart=Smartphone("iphone","14 pro",130000)
smart.show()
