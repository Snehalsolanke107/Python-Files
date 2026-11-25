# Abstraction 
    # hide complex and  uneccessary data to user
    #  eg phone pick , hide code of print Function
    # there are three main concept in abstraction 
        # 1. abstract class
            #  it is collection of abstract method and non abstract method(user define method)
            # we can create object of abstract class when no abstract method present
        # 2. Abstract method  : decorator (@abstractmethod)
        # 3. interface
            #  it is collection of only abstract method
    #  wer can create abstract class or abstract method using abc module (ABC class )

from abc import ABC ,abstractmethod

class Demo(ABC) :
    def __init__(self, name , age):
        self.name = name
        self.age = age

    @abstractmethod
    def Display_details(self):
        print(f"name : {self.name} age : {self.age}")

    def _showInfo(self):
        print(f"name : {self.name}")

    def __add__(self, other):
        total_age = self.age + other.age
        print(total_age)

# d1 = Demo("roshan", 36)
# d1.Display_details()

class Demo1(Demo):
    def __init__(self, name, age):
        super().__init__(name, age)

    def Display_details(self):
        return super().Display_details()

d2 = Demo1("Roshani",28)
d2.Display_details()
d2._showInfo()