# 8. Design a system where a base class `Animal` has a method `speak()`, 
# and subclasses `Dog` and `Cat` override it.

class Animal:
    def __init__(self,type):
        self.type=type
    def speak(self):
        print(f"{self.type} can speak")
class Dog(Animal):
    def __init__(self,type,sound):
        super().__init__(type)
        self.sound=sound
    def speak(self):
        print(f"Dog {self.sound}")
class Cat(Animal):
    def __init__(self,type,sound):
        super().__init__(type)
        self.sound=sound
    def speak(self):
        print(f"Cat {self.sound}")

dog=Dog("pet","barks")
dog.speak()
cat=Cat("pet","meow")
cat.speak()