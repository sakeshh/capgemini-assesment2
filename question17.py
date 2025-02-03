# 17. Define an abstract class `IDatabaseOperations` with methods `insert()`, 
# `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class SQLdatabase(IDatabaseOperations):
    def insert(self):
        print("inserted")
    def update(self):
        print("updated")
    def delete(self):
        print("deleted")
class Nosqldatabase(IDatabaseOperations):
    def insert(self):
        print("inserted")
    def update(self):
        print("updated")
    def delete(self):
        print("deleted")
idop=Nosqldatabase()
idop.insert()
idop.update()
idop.delete()
ido=SQLdatabase()
ido.insert()
ido.update()
ido.delete()