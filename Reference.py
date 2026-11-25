# how attribute access

class student:
    def __init__(self,name):
        self.name = name


s1 = student("Snehal")
print(s1.name)

class Test:
    x = 10

t = Test()
print(t.x)

class A:
    def show(self):
        print("Hello")
obj = A()
obj.show()

# Attribute creation from the outsite the class

class student:
    pass

s1 = student()
s1.age = 21
print(s1.age)
s2 = student()
print(s2.age) # 'student' object has no attribute 'age'

# reference variable

class student:
    pass

s1 = student()
print(s1) # 0x0000022642167230>
s2 = s1

s2 = student()
print(s2) # 0x00000226423E8CD0>

class student:
    pass

s1 = student() # 0x000002B547297230>
print(s1) 
s2 = student() # 0x000002B547297230>
s2 = s1
print(s2) 

a = [1,2,3]
print(a)
print(id(a))

b = a
print(b)
print(id(b))
print(a is b)
