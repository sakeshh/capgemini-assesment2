# 1. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.

class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def show(self):
        print(f"employee name:{self.name} id:{self.id} department:{self.department}")
num=int(input("enter number of employees"))
emp_list=[]
for i in range(num):
    
    emp=Employee(name=input("enter name of employee"),id=input("enter id"),department=input("enter department"))
    emp_list.append(emp)
for i in emp_list:
    i.show()

