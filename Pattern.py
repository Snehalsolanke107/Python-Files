# Nested for loop

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,j)

# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end="")

# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end="")
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end="")
#     print()

# Matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in Matrix:
#     for element in row:
#         print(element,end=" ")
#     print()

# num = 4
# for i in range(num):
#     for j in range(num):
#         print("*",end=" ")
#     print()

# num = 4
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         print(j*j,end=" ")
#     print()

# num = 4
# for i in range(num):
#     for j in range(num):
#         print(chr(65+i),end=" ")
#     print()

# num = 4
# for i in range(num):
#     for j in range(num):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     ch = "a"
#     name = chr(ord(ch)+i-1)
#     for j in range(1,6):
#         print(name,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         ch = "a"
#         name = chr(ord(ch)+j-1)
#         print(name,end=" ")
#     print()

# a b c d e 
# a b c d e 
# a b c d e 
# a b c d e 
# a b c d e 

# for i in range(1,6):
#     for j in range(1,6):
#         print(j*j,end=" ")
#     print()

# 1 4 9 16 25 
# 1 4 9 16 25 
# 1 4 9 16 25 
# 1 4 9 16 25 
# 1 4 9 16 25 

# for i in range(1,6):
#     for j in range(1,6):
#         if j <= i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")

# *         
# * *       
# * * *     
# * * * *   
# * * * * * 

# for i in range(1,6):
#     for j in range(1,6):
#         if j <= 6-i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")

# * * * * * 
# * * * *   
# * * *     
# * *       
# *      

# for i in range(1,6):
#     for j in range(1,6):
#         if j >= 6-i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

# for i in range(1,6):
#     for j in range(1,6):
#         if j >= i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")

# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         *  

# for i in range(1,6):
#     for j in range(1,6):
#         if j <= i:
#             print(i,end=" ")
#         else:
#             print(" ",end=" ")
#     print("")

# 1         
# 2 2       
# 3 3 3     
# 4 4 4 4   
# 5 5 5 5 5 

# for i in range(1,6):
#     for j in range(1,6):
#         if j <= i:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print("")

# 1         
# 1 2       
# 1 2 3     
# 1 2 3 4   
# 1 2 3 4 5

# for i in range(1,5):
#     for j in range(1,8):
#         if j >= 5-i and j <= 3+i :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")

#    *   
#   ***  
#  ***** 
# *******
