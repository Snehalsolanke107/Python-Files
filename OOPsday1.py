# OOPS 
# stand for object oriented Programming Language
# it is programming paradigm used to wrap up data(variable)  and methoda (function) in single unit 
# single unit means class
# oops use in real world Entity eg car

# there are Four main concept 
# 1. class
    # it is blueprint of object 
    #  we cannot pass memory of class
    # create class using class keyword
    # we can create method inside class first parameter always consider as reference variable
# 2. Object
    # instance of class 
    # We can pass memory of object

# Constructor /Mangic method
    #  we can create object constructor internal  call automatically

# self parameter 
    # self is reference Variable
    #  used to refer class object 

# major pillers of OOPS
# 1. Inhertance (parent child relation)
# 2. Encapsulation(bind data in single unit)
# 3. polymorphism (many forms)
# 4. Abstraction (HIde complex Data)

# Types of variable
# 1. Class Variable (global )
# 2. instance variable (intilize in constructor)
# 3. Local variable 

# Types of method
# 1. class method
# 2. static method
# 3. instance Method

# class Demo:
#     def Addition(ritik ):
#         # add = num2
#         return "Addition Method"
    
#     def Addition1( self,  num1, num2):
#             add = num1 + num2
#             return add

# d1 = Demo()
# print(d1.Addition())
# print(d1.Addition1(20,30))


class Demo2:
    sname = "TKA"   # class variable
    add = "Chinchwad Pune" # class variable

    def __init__(self, name , age):  # constructor  (instance method)
        self.name = name  # instance variable
        self.age = age   # instance variable

    def Info(self):
        return f"Student Name : {self.name} Student age : {self.age}"

    @classmethod
    def SchoolInfo(manjot):
        return f"School name : {manjot.sname} School Address : {manjot.add}"

    def Addition(self, num1, num2): # local Variable
        return num1 + num2

    @staticmethod
    def Person_info(name, age):
        return f"person name :  {name} person Age : {age}"

                    #  Instance Variable / method

# d2 = Demo2("Roshan",35)
# d2.__init__("Pratik", 30)
# print(d2.Info())

# print(Demo2("Rohan", 36).Info())

# print(f"use object : {d2.name}")
# print(f"use class name : {Demo2("Roshani", 25).name}")

                    #  class Variable / method
# d3 = Demo2()
# print(f"use object : {d3.sname}")
# print(f"use class name : {Demo2.sname}")
# print(d3.SchoolInfo())
# print(f"use class name : {Demo2.SchoolInfo()}")


                    #  Local Variable / static method


# d4 = Demo2()
# print(d4.Addition(10,20))

# # d4.num1
# print(d4.Person_info("Nilesh", 25))

# print(d4.n)


# d5 = Demo2("Ganesh", 21)

# d5.name = "Ritik"

# print(d5.Info())

# d5.sname = "SBI"

# print(d5.SchoolInfo())

