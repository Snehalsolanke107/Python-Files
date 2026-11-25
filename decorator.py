# Decorator = function modify/enhance

# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello")
# greet()

def my_decorator(func):
    def wrapper(name):
        print("Before function call")
        func(name)
        print("After function call")
    return wrapper

@my_decorator
def greet(name):
    print("Hello",name)

greet("Snehal")

def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Hello")
        result=func(*args,**kwargs)
        print("After result")
        return result
    return wrapper

@my_decorator

def add(a,b):
    return a+b
result = add(5,3)
print(result)

add()