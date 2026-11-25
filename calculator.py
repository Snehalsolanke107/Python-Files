def Addition(num1, num2):
    add = num1 + num2
    print(f"{num1} + {num2} = {add}")

def Multiplication(num1, num2):
    multi = num1 * num2
    print(f"{num1} * {num2} = {multi}")

def Division(num1, num2):
    div = num1 / num2
    print(f"{num1} / {num2} = {div}")


class Student_info:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name 

    def Display_Student(self):
        print(f"student name : {self.name} , Student Roll NO : {self.rollno}")


keyword = ["if", "else","elif","for","while"]

import pandas 

df  = pandas.DataFrame([1,2,3,4])
print(df)