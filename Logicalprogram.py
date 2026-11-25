#1] Write a Python program to reverse a number.

# By using while loop
num = int(input("Enter the number :"))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)
# ------------------------------------------------------------------------------------

# By using for loop
num = int(input("Enter the number :"))
num_str = str(num)
reverse = ""

for i in num_str:
    reverse = i + reverse

print("Original Number:", num)
print("Reversed Number:", reverse)
# ------------------------------------------------------------------------------------

#2] A palindrome number reads the same forward and backward.

# By using while loop
num = 121 
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
# ------------------------------------------------------------------------------------

# By using for loop
num = int(input("Enter a number: "))

num_str = str(num)
reverse = ""

for i in num_str:
    reverse = i + reverse

if num_str == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
# ------------------------------------------------------------------------------------

# 3] A string palindrome  

# By using while loop
string = input("Enter a string: ")

reverse = ""
i = len(string) - 1

while i >= 0:
    reverse = reverse + string[i]
    i = i - 1

if string == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
# ------------------------------------------------------------------------------------

# By using for loop
num = input("Enter a number: ")
original = ""

for i in num:
    original = i+original
print(original)

if num == original:
    print("Palindrome")
else:
    print("Not Palindrome")
# ------------------------------------------------------------------------------------

# By using without loop
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
# ------------------------------------------------------------------------------------

#4] Count the number of digits

# By using for loop
num = int(input("Enter a number :"))
count = 0

for i in str(num):
    count = count + 1

print("Number of digits:",count)
# ------------------------------------------------------------------------------------

# By using while loop
num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count = count + 1

print("Number of digits:", count)
# ------------------------------------------------------------------------------------

#4] Check Whether a Number is Armstrong

# By using while loop
num = int(input("Enter a number: "))

original = num
power = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** power
    num = num // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# ------------------------------------------------------------------------------------

# By using for loop
num = int(input("Enter a number: "))

num_str = str(num)
power = len(num_str)
total = 0

for digit in num_str:
    total = total + int(digit) ** power

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# ------------------------------------------------------------------------------------

# 5] Find Factorial of a Number

# By using for loop
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial of", num, "is", factorial)
# ------------------------------------------------------------------------------------

# By using while loop
num = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= num:
    factorial = factorial * i
    i = i + 1

print("Factorial of", num, "is", factorial)
# ------------------------------------------------------------------------------------

# 6] Check Prime Number = which no. is divide by 1 & itself.

# By using for loop
num = int(input("Enter a number: "))

for i in range(2,num+1):
    if num % i == 0:
        print("Not a Prime number")
    else:
        print("Prime number")
# # ------------------------------------------------------------------------------------

# By using while loop
num = int(input("Enter a number: "))
i = 2
count = 0

while num > 0:
    if num % i == 0:
        count = count + 1
    i = i + 1
if count == 0 and num > 1:
    print("Prime number")
else:
    print("Not a Prime number")    
# # ------------------------------------------------------------------------------------

# 7]check number is perfect or not = divide all no. then check add of total number is same as that number.

# By using for loop
num = int(input("Enter a number: "))
sum = 0 

for i in range(1,num):
    if num % i == 0:
        sum = sum + i
        print("sum")
if num == sum:
    print("It is perfect number.")
else:
    print("It is not perfect number.")
# # ------------------------------------------------------------------------------------

# By using while loop
num = int(input("Enter a number: "))
i = 0
sum = 0 

while i < num:
    if num % i == 0:
        sum = sum + i
        print("sum")
    i = i + 1

if num == sum:
    print("It is perfect number.")
else:
    print("It is not perfect number.")

# # ------------------------------------------------------------------------------------

# 8]fibonacii series = all range numbers check their addition.

# By using for loop
no = int(input("Enter a number: "))
num1 = 0
num2 = 1

for i in range(no):
    print(num1,end="_") 
    temp = num1
    num1 = num2
    num2 = temp + num1

    num1,num2 = num2,num1 + num2
# # ------------------------------------------------------------------------------------

# By using while loop

no = int(input("Enter a number: "))
num1 = 0
num2 = 1 
count = 0
while count < no:
    print(num1,end="_")
    num1,num2 = num2,num1 + num2
    count = count + 1
# # ------------------------------------------------------------------------------------

# 9]Factorial = The factorial of a number n is the multiplication of all positive numbers from 1 to n.

# By using for loop
num = int(input("Enter a number: "))
fact = 1

for i in range(1,num+1):
    if i >= 1:
        fact = fact *i       
    print("Factorial is : ",fact)
# # ------------------------------------------------------------------------------------

# By using while loop
num = int(input("Enter a number: "))
fact = 1

while num > 0:
    fact = fact * num
    print(fact)
    num = num - 1
print("Factorial is : ",fact)
# # ------------------------------------------------------------------------------------

# 10]Reverse a String

# By using for loop
str = (input("Enter a String: "))

for i in str:
    str = str[::-1]
    print(str)
# # ------------------------------------------------------------------------------------

# By using while loop
str = (input("Enter a String: "))
reverse = ""
i = len(string) - 1
while i >= 0:
    reverse = reverse + string[i]
    i = i - 1

print("Reversed string:", reverse)
# # ------------------------------------------------------------------------------------

# 11]prime number range 

# By using for loop
num = int(input("Enter a string :"))
for i in range (2,num+1):
    count = 0

    for i in range(2,num+1):
        if num % i == 0:
            count += 1

    if count == 2:
        print(num,end="_")

# # ------------------------------------------------------------------------------------

# By using while loop
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

num = start

while num <= end:
    i = 2
    is_prime = True

    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime and num > 1:
        print(num, end=" ")

    num += 1
# # ------------------------------------------------------------------------------------

# By using for loop
# # ------------------------------------------------------------------------------------
# By using while loop
# # ------------------------------------------------------------------------------------
# By using for loop
# # ------------------------------------------------------------------------------------
# By using while loop
# # ------------------------------------------------------------------------------------
# By using for loop
# # ------------------------------------------------------------------------------------
# By using while loop
# # ------------------------------------------------------------------------------------
# By using for loop
# # ------------------------------------------------------------------------------------
# By using while loop
# # ------------------------------------------------------------------------------------
# By using for loop
# # ------------------------------------------------------------------------------------
# By using while loop
# # ------------------------------------------------------------------------------------
# By using for loop
# # ------------------------------------------------------------------------------------
# By using while loop
# # ------------------------------------------------------------------------------------
# By using for loop
# # ------------------------------------------------------------------------------------
# By using while loop
# # ------------------------------------------------------------------------------------
# By using for loop
# # ------------------------------------------------------------------------------------
# By using while loop
# # ------------------------------------------------------------------------------------
# By using for loop
# # ------------------------------------------------------------------------------------
# By using while loop
# # ------------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------
# # ------------------------------------------------------------------------------------


