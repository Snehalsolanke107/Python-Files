# Inheritance 
    # child class aquire property of parent class
    # property means methods and variable
    # use super method to access parent class property
    # two main concept in inheritance 
        # 1. is-a relationship
        # 2. has-a relationship
    # Types of Inheritance 
        # 1. single/simple inheritance
        # 1. multiple inheritance
        # 3. multilevel inheritance
        # 4. hybrid inheritance
        # 5. hirarchical inheritance 

class Parent:
    pcv = "Parent"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Parent_info(self):
        print(f"parent name : {self.name} , parent age : {self.age}")

    def  Addition(self , num1 ,num2):
        add = num1 + num2
        print(f"addition of {num1} + {num2} = {add}")

    @staticmethod
    def StaticMethod(num3 ,  num4):
         print(f"addition of {num3} + {num4} = {num3*num4}")

p1 = Parent("Roshan" , 35)
# p1.Addition(10,20)
# p1.Parent_info()
        
class Child(Parent):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        super().Parent_info()
        super().Addition(20,30)
        # print(super().name)
        # print(super().age)
        print(super().pcv)

        super().StaticMethod(10,20)

        self.city = city


    def Child_info(self):
            print(f"parent name : {self.name} , parent age : {self.age}  child city : {self.city}")

# c1 = Child("Roshani", 30 , "Pune")
# c1.Parent_info()
# c1.Child_info()

class Child1:
     def __init__(self, name , age):
        #   Parent("Rohan", 28).__init__(name, age)
        #   Parent("Rohan", 28).Parent_info()
        #   Parent("Rohan", 28).Addition(10,20)
        #   Parent("Rohan", 28).StaticMethod(20,30)
        #   print(Parent("Rohan", 28).pcv)

        p1.Parent_info()
        p1.StaticMethod(20,3)
        p1.Addition(10,20)
        print(p1.pcv)
        print(p1.name)
        print(p1.age)
        # p1.__init__()

c2 = Child1("Rohan", 28)