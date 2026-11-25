# # Single inheritance

# class Father:
#     def house(self):
#         print("Father has a house")

# class son(Father):
#     def car(self):
#         print("Son has a car")

# s = son()
# s.car()
# s.house()

# # Multi-level inheritance

# class GrandFather:
#     def land(self):
#         print("GrandFather has a land")
# class Father(GrandFather):
#     def house(self):
#         print("Father has a house")

# class son(Father):
#     def car(self):
#         print("Son has a car")

# s = son()
# s.car()
# s.house()
# s.land()

# # Multiple inheritance

# class Father():
#     def Fshow(self):
#         print("Father has a house")

# class Mother():
#     def Mshow(self):
#         print("Mother has a car")

# class son(Father,Mother):
#     def Sshow(self):
#             print("Son has a bike")

# s = son()
# s.Fshow()
# s.Mshow()
# s.Sshow()

# # Hierarchical inheritance

# class Father():
#     def Fshow(self):
#         print("Father has a house")

# class Aditya(Father):
#     def Ashow(self):
#         print("Aditya has a car")

# class Ajay(Father):
#     def ashow(self):
#         print("Ajay has a bike")

# a = Aditya()
# a.Fshow()
# a.Ashow()

# b = Ajay()
# b.Fshow()
# b.ashow()

# # Hybrid inheritance = Multiple & Multi-level

# class A:
#     def __init__(self):
#         print("A constructor")

# class B(A):
#     def __init__(self):
#         print("B Constructor")
#         super().__init__()

# b = B()

# # Method overriding

# class A:
#     def sound(self):
#         print("A method")

# class B(A):
#     def sound(self):
#         print("B method")
# b = B()
# b.sound()
# b.sound()

# # Super Method

# class A:
#     def sound(self):
#         print("A method")

# class B(A):
#     def sound(self):
#         super().sound() # call the method from class A
#         print("B method")
# b = B()
# b.sound()
# b.sound()

# collage management system

class Person:
    def __init__(self,name):
        self.name = name
    def display(self):
        print("Name",self.name)

class student(Person):
    def __init__(self, name,rollno):
        super().__init__(name)
        self.rollno = rollno

    def display(self):
        super().display()
        print("Roll no :",self.rollno)
        
s1 = student("Jayesh",101)
s1.display()
