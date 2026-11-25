# getter and setter method = private member access outside the class

class Bank:
    def __init__(self,name,balance):
        self.name = name 
        self.__balance = balance

    # getter method 
    def get_balance(self):
        return self.__balance

    # setter method
    def set_balance(self,balance):
        self.__balance = balance

acc1 = Bank("Snehal",100000)
acc1.__balance = 50000
print(acc1.name)

print(acc1.__balance)
print(acc1.get_balance)

print(acc1.set_balance(50000))
print(acc1.get_balance())

