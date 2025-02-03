#2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods.
 #Implement logic to prevent overdraft.
class Bankaccount:
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,withd):
        if self.balance>withd:
            self.balance-=withd
            print(f"total bank balance is {self.balance}")
        else:
            print("available balance is low ")
    def deposit(self,dep):
        self.balance+=dep
        print(f"total account balance is:{self.balance}")
bank=Bankaccount(2000)
bank.withdraw(200)
bank.deposit(500)



