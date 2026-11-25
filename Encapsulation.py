# Encapsulation 
    # we can hide and bind data into single unit
    #  we can achive encapsulation using  access specifire / modifires
    # Types of access modifires 
        # 1. public  eg num1 , num2 , Addition() , Square()
        # 2. protected (_) eg _num1 , _num2 , _Addition(), _Square()
        # 3. privet (__)  eg __num1 , __num2 , __Addition(), __Square()

class Vehicle:
    color = "Blue"
    _Enginestroke = "two stroke"
    __type = "gear"


# v = Vehicle()
# v.color = "Red"
# print(v.color)
# # v._Enginestroke= "Four stroke"
# print(v._Enginestroke)
# print(v.__type)  # AttributeError: 'Vehicle' object has no attribute '__type'

# v.Gear_info("Four stroke")

class Car(Vehicle):
    def Vehicle_info(self):
        print(super().color)
        print(super()._Enginestroke)
        # print(super().__type) # AttributeError: 'super' object has no attribute '_Car__type'

# c = Car()
# c.color = "Red"
# c.Vehicle_info()

class Bike:
    def Bike_info(self):
        print(Vehicle.color)
        print(Vehicle._Enginestroke)
        # print(Vehicle.__type)
# b= Bike()
# b.Bike_info()


class Bank:
    def __init__(self , cname, bal):
        self.__cname = cname
        self.__bal = bal

    def _CustomerInfo(self):
        print(f"customer name : {self.__cname} , customer balance : {self.__bal}")

    def __CustomerInfo1(self):
        print(f"customer name : {self.__cname} , customer balance : {self.__bal}")

    def ShowUser(self):
        self.__CustomerInfo1()
        print(self.__cname)

b1 = Bank("Roshan", 20000)
# b1._CustomerInfo()
# # b1.__bal
# # b1.__cname
# b1.__CustomerInfo1()
# print(b1._Bank__cname)

class SBI(Bank):
    def __init__(self, cname, bal):
        super().__init__(cname, bal)
        # super()._CustomerInfo()
        # super().__CustomerInfo1() # AttributeError: 'super' object has no attribute '_SBI__CustomerInfo1'
        super().ShowUser()
# s = SBI("Rohan", 35000)
# print(s._Bank__cname)


d = {1:1,2:4,3:9}
print(d.items())