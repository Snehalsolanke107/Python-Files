# pre defined functions.
# two ways print of return 
# def add(a,b):
#     return a + b
# r = add(4,5)
# print(r)

# def add1(a,b):
#     return a + b
# add1(4,5)
# print(add1(4,5))

# function with default paramenter

def add(a,b =5):
    return a + b

print(add(6,5))
r = add(4)
print(r)

# even odd check function

def iseven(num):

    if num % 2 == 0:
        print("Even")
    else:
        print("odd")

iseven(20)

num1 = int(input("Enter  the first number:"))
num2 = int(input("Enter  the second number:"))
num3 = int(input("Enter  the third number:"))

def maxfind(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

r = maxfind(num1,num2,num3)
print("Max of three number :",r)

def EvenNo():
    for i in range(0,10):
        if i % 2 == 0:
            print(i)

EvenNo()

num3 = 10 # Global Variable
def Multiplication():
    num4 = 3 # local Variable
    global num3
    num3 = 50
    mul = num3 * num4
    print(mul)
Multiplication()

