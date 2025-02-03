# 13. Develop a `Shape` class with a method `area()`.
#  Implement `Square` and `Triangle` classes that provide specific 
# implementations for `area()`.
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        super().__init__()
        self.side=side
    def area(self):
        area=self.side*self.side
        print(f"area:{area}")
class Triangle(Shape):
    def __init__(self,base,height):
        super().__init__()
        self.base=base
        self.height=height
    def area(self):
        area=0.5*self.base*self.height
        print(f"area:{area}")
square=Square(10)
square.area()
triangle=Triangle(10,50)
triangle.area()



