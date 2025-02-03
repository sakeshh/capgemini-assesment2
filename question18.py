# 18. Implement an abstract class `ICalculator` with methods `add()`,
#  `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator`
#  class that implements these methods.
from abc import ABC,abstractmethod
class Icalculator(ABC):
    @abstractmethod
    def add():
        pass
    @abstractmethod
    def sub():
        pass
    @abstractmethod
    def mul():
        pass
    @abstractmethod
    def div():
        pass
class Basiccal(Icalculator):
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
basic=Basiccal(20,10)
print(basic.add())
print(basic.sub())
print(basic.mul())
print(basic.div())
