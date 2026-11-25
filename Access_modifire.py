# public access modifiers

class student:
    def __init__(self):
        self.name = "Snehal" # public variable

    def show(self):
        print(self.name)


obj = student()
print(obj.name)
obj.show()

# protected access modifiers (_)
# inheriate the class

class student:
    def __init__(self):
        self._name = "Snehal" # protected variable

    def show(self):
        print(self._name)


obj = student()
print(obj._name)
obj.show()

class child(student):

    def display(self):
        print(self._name)

c = child()
c.display()
print(c._name)

# private access modifiers (__)
# don't access outside the class

class student:
    def __init__(self):
        self.__name = "Snehal" # private variable

    def show(self):
        print(self.__name)

class child(student):

    def display(self):
        print(self.__name)

c = child()
c.display()
# print(c.__name)

print(obj._student__name) # by name mingling method access

# ------------------------------------------------------------------------------------------------------------

class Bank:
    def __init__(self):
        self.name = "Snehal"
        self._balance = 5000
        self.__pin = 1234

    def showdetails(self):
        print(self.name,self._balance,self.__pin)

obj = Bank()
print(obj.name)

obj._balance = 50000
print(obj._balance)

# print(obj.__pin)
obj.showdetails()
print(obj._Bank__pin)