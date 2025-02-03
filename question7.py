# 7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, 
# where `Manager` has an additional method `approve_leave()`.


class Person:
    def __init__(self,company):
        self.company=company
    def show(self):
        print(f"person works in {self.company}")
class Employee(Person):
    def __init__(self, company,days_worked,leaves_taken):
        super().__init__(company)
        self.days_worked=days_worked
        self.leaves_taken=leaves_taken
    def showE(self):
        print(f"Person worked for {self.days_worked} days and took leave for {self.leaves_taken} days")
class Manager(Employee):
    def __init__(self, company, days_worked,leaves_taken,leaves_allowed):
        super().__init__(company, days_worked,leaves_taken)
        self.leaves_allowed=leaves_allowed
    def approve_leave(self):
        if self.leaves_taken<=self.leaves_allowed:
            return "leave approved"
        else:
            return "leave denied"
manager=Manager("capgemini",40,5,6)
print(manager.approve_leave())
