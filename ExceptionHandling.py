# Exception Handling 
    # solve error by using try and except block
    # handle abnormal condition
    #  handle runtime error

# Error (exception) :
# unwanted and unexcepted part distrub the normal flow of program
#  1. runtime 
#  2. syntax 
#  3. logical error

# Exception Handling 
#  handle unwanted and unexcepted part do not  distrub the normal flow of program
# We can use multiple block  try except finally else 
# one keyword raise

# num1 = 10
# num2 = 0
# try : 
#     print(num1 / num2)
# except Exception as e :
#     print(e)

# else :
#     print("operation success!!")
# finally :
#     print("Welcome")


# try : 
#     num3 = int (input("Enter a age"))
#     if num3 >= 18:
#         print("Eligible")
#     else :
#         raise Exception
# except Exception as e :
#     print(e)


# l1 = [10,20,30]
# try : 
#     # print(l1.pop(5))

#     print(l1.remove(100))
# except IndexError as e :
#     print(e)

# except ValueError as e :
#     e = "Value not found"
#     print(e)

# print("Operation success")


l1 = [10,20,30]

print(l1 + 5)