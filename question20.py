# 20. Write a scenario where a `UserAuthentication` interface contains 
# `login()` and `logout()` methods, and it is implemented 
# by `GoogleAuth` and `FacebookAuth` classes.

from abc import ABC,abstractmethod
class Userauthentication(ABC):
    @abstractmethod
    def login():
        pass
    @abstractmethod
    def logout():
        pass

class Googleauth(Userauthentication):
    def login(self):
        print("logged into google")
    def logout(self):
        print("logged out of google")
class Facebookauth(Userauthentication):
    def login(self):
        print("logged into facebook")
    def logout(self):
        print("logged out of facebook")
google=Googleauth()
google.login()
google.logout()
facebook=Facebookauth()
facebook.login()
facebook.logout()
    