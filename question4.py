# 4. Implement a `Student` class with a constructor that initializes `name` and
#  `roll_number`. Write a method to return student details.
class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def student_details(self):
        return self.name,self.roll_number
    
student=Student("sakesh","66D5")
print(student.student_details())