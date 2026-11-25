# Polymorphism
    # we can create many forms of methods and variable
    # greek poly : many morphs : forms
    # types of polymorphism
        # 1. compile time (overloading)(static type)(use single class)
                # method overloading : not supported
                # constructor overloding : not supported
                # operator overloading  : Support
        # 2. run  time (overrding)(dynamic type)(use inherite class)
                # method overrding : support 
                

class Parent:
    def __init__(self , name):
        self.name = name
        print(self.name)

    def __init__(self , name , age):
            self.name = name
            self.age = age
            print(self.name ,"   " ,self.age)

# p1 = Parent("Roshan", 35)
# p2 = Parent("Roshani")

class Parent1:
     def Square(self, num1):
          print(num1 * num1)

     def Square(self, num1,num2):
               print(num1 ** num2)
# p3 = Parent1()
# p3.Square(3,3)
# p3.Square(6)


class StudentInfo:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def StudentInfo(self):
          print(f"Student name : {self.name} , Student Age : {self.age}")

    def __add__(self, other):
          agesum= self.age + other.age
          print(agesum)

    def __div__(self, other):
              agesum= self.age / other.age
              print(agesum)

# s1 = StudentInfo("Pratik", 30)
# s1.StudentInfo()  

# s2 = StudentInfo("Rohan", 28)
# s2.StudentInfo()  

# s1 + s2

# # s1 / s2

# s1.__div__(s2)


class IPL:
      def Player(self):
            print("IPL player method")

class WPL(IPL):
      def Player(self):
                  print("WPL player method")

w1 = WPL()
w1.Player()