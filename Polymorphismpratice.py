
# # operator overloading

# print(10+5)
# print("hello"+"snehal")
# print([1,2]+[3,4])
# print((1,2)+(3,4))

# # custom operator overloading

# class student:
#     def __init__(self,marks):
#         self.marks = marks

#     def __add__(self, other):
#         return self.marks + other.marks

# s1 = student(50)
# s2 = student(30)
# print(s1+s2)

# # method overriding (run time polymorphism)

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         super().sound() # call parent class method
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         super().sound() # call parent class method
#         print("Cat meows")

# a = Animal()
# a.sound()
# d = Dog()
# d.sound()
# c = Cat()
# c.sound() 

# Duck typing polymorphism = defining a method that can work with any object that has the 
# required attributes or methods, regardless of its type

# class laptop:
#     def code(self):
#         print("coading on laptop")

# class Mobile:
#     def code(self):
#         print("coading on mobile")

# def perform_coading(device):
#     device.code()

# l = laptop()
# m = Mobile()
# perform_coading(l)
# perform_coading(m)
# It walks like duck and it quacks like a duck, then it mut be a duck.

class Math:
    def add(self,a,b,c=0):
        return a+b+c

    # def add(self,a,b,c,d=0):
    #     return a+b+c+d

m = Math()
print(m.add(1,2))
print(m.add(1,2,3))