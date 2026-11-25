# Types of programming

# 1] procedural programming = step by step instruction. ex-c, pascal, Basic

# 2] OOP programming = real word program ex- python, c#
# It contains class and objects

# 3] Functional programming = 

# 4] Logic programming = 

# 5] Event Driven programming = 



class student:

    def __init__(self,name,age): # Prameterized constructor
          self.name = name
          self.age = age

    def getshow(self):
          print(self.name,self.age)

    def show(self):
            print(self.school_name)

s1 = student("Snehal",23)
s1.getshow()
s1.show()

class student1:
      def __init__(self): # default constructor
                self.school_name = "ABC"
                print(self.school_name)

s2 = student1()

# Attributes/Variables

class student2:
      collage = "KBT" # class Variable
      
s1 = student2()
print(s1.collage)
s2 = student2()
s2.collage = "RYK"
print(s2.collage)  

class student3:
      def __init__(self,name):
            self.name = name # instance Variable

s1 = student3("Snehal")
s2 = student3("Vishwjeet")

print(s1.name)
print(s2.name)

# methods

class student4:
    def __init__(self,name):   # instance method
       self.name = name

    def show(self):      # instance method
        print(self.name)

s1 = student4("Snehal")
s1.show()
s2 = student4("Vish")
s2.show()

