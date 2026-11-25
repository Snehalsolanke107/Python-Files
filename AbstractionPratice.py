#Hiding internal details & showing only essential features.

# Use ABC Model & Abstract Method
# ABC = Abstract base class 
#Abstract Method decorator

# Abstract class = only declear method,no implementation,no object creation

from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def checkbalance(self,amount):
        pass

class SBI(Bank):
    def __init__(self,balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited")

    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance -= amount
            print("withdraw : ",amount)
        else:
            print("Insufficient Balanve")

    def checkbalance(self):
        print("Your current balance : ",self.balance)

acc = SBI(1000)
acc.deposit(5000)
acc.withdraw(500)
acc.checkbalance()