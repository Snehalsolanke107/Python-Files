class student:
    collage = "KBT"

    @classmethod
    def change_collage(cls,new_name):
        cls.collage = new_name

    @staticmethod
    def add(a,b):
        return a + b

student.change_collage("MIT")
print(student.collage)
print(student.add(5,3))

#instance method = work on object
#class method = work on class
#static method = work on utility don't acces any thing 

# Question
# Product stores :

# 1 Design 2 create an online store for Products (name, price)

# 2 Track Total product created

# 3 create a static method to calculate 3 discount on each produd based on a parameter

class Product:
    count = 0 # class variable
    def __init__(self,name,price):
        self.name = name # instance variable
        self.price = price # instance variable
        Product.count += self.count

    def get_info(self): # instance method
        print(self.name,self.price)

    @classmethod # class method
    def get_count(cls):
        print("Total product = " ,cls.count)

    @staticmethod # static method
    def discount(price,per):
        dis = price-(price*per)/100
        print("Discounted price = " ,dis)

p1 = Product("Pen",2)
p1.get_info()
p2 = Product("Notebook",45)
p2.get_info()
Product.get_count()
Product.discount(5000,20)