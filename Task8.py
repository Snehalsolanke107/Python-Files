# 1.Even-Odd Checker
# Write a program that takes a number as input and checks whether it is even or odd.

num1 = int(input("Enter a number : "))
if num1 > 0:
    if num1 % 2 == 0:
        print("It is an even number.")
    elif num1 % 2 == 1:
        print("It is a odd number.")
else:
    print("Enter a Valid input")

# 2.Positive, Negative, or Zero
# Write a program that asks the user to enter a number and checks whether it is positive, negative, or zero.

num1 = int(input("Enter a number : "))
if num1 > 0:
    print("It is a positive number.")
elif num1 < 0:
    print("It is a negative number.")
else:
    print("It is a Zero.")

# 3.Voting Eligibility
# Ask the user for their age. If age is greater than or equal to 18, print "Eligible to vote", otherwise print "Not eligible to vote".

num1 = int(input("Enter a number : "))
if num1 > 0 and num1 <= 100:
    if num1 >= 18 and num1 <= 70:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
else:
    print("Enter a Valid input")

# 4.Maximum of Two Numbers
# Take two numbers from the user and use if-else to find which one is greater.

num1 = int(input("Enter First number : "))
print("First number is :",num1)

num2 = int(input("Enter second number : "))
print("Second number is :",num2)

if num1 > num2:
    print("First number is bigger than Second number.")
else:
    print("Second number is bigger than First number.")

# 5.Pass or Fail
# Ask the user for their marks. If marks are greater than or equal to 40, print "Pass", else print "Fail".

marks = int(input("Enter a Marks :"))
print("Marks is :",marks)

if marks > 0 and marks <= 100:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Enter a Valid Marks")

# 6.Divisibility Check
# Write a program that takes a number from the user and checks:
# 	If divisible by 3 → print "Divisible by 3"
# 	If divisible by 5 → print "Divisible by 5"
# 	If divisible by both → print "Divisible by 3 and 5"
# 	Otherwise → print "Not divisible by 3 or 5"

num1 = int(input("Enter a number : "))
print("Number is :",num1)

if num > 0:
    if num1 % 3 == 0:
        print("Divisible by 3")
    elif num1 % 5 == 0:
        print("Divisible by 5")
    elif num1 % 3 == 0 and num1 % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not divisible by 3 or 5")
else:
    print("Enter Valid Number")

# 7.Grade Calculator
# Take marks as input and assign grades:
# 	90 and above → A
# 	75–89 → B
# 	60–74 → C
# 	40–59 → D
# 	Below 40 → Fail

Marks = int(input("Enter a Marks :"))
print("Marks is :",Marks)

if Marks > 0 and Marks >= 100:
    if Marks >= 90 and Marks <= 100:
        print("Grade A")
    elif Marks >= 89 and Marks <= 75:
        print("Grade B")
    elif Marks >= 74 and Marks <= 60:
        print("Grade C")
    elif Marks >= 59 and Marks <= 40:
        print("Grade D")
    else:
        print("Fail")
else:
    print("Enter a Valid Marks")

# 8.ATM Withdrawal
# Ask the user to enter the balance and withdrawal amount. 
# If withdrawal amount ≤ balance, deduct it and print remaining balance, else print "Insufficient Balance".

balance = int(input("Enter a balance :"))
print("Balance is :",balance)

withdrawal_amount = int(input("Enter a withdrawal amount :"))
print("Withdrawal amount is :",withdrawal_amount)

if withdrawal_amount <= balance:
    balance = balance - withdrawal_amount
    print("Remaining Balance =", balance)
else:
    print("Insufficient Balance")

# 9.Login System
# Store a username and password. Take input from the user. If both match, print "Login Successful", else print "Invalid Credentials".

Stored_name = "Snehal"
Stored_password = "10242003"

username = input("Enter  your Username :")
print("Username is :",username)

password = input("Enter  your Password :")
print("Password is :",password)

if Stored_name == username:
    print("Login Successful")
else:
    print("Invalid Credentials")

# 10.Discount Calculator
# A shop gives discount based on amount:
# •	More than 5000 → 20% discount
# •	2000–5000 → 10% discount
# •	Below 2000 → No discount
# Calculate final bill.

amount = float(input("Enter the bill amount: "))
print("Bill amount is :",amount)

if amount > 5000:
    discount = amount * 20/100
elif amount >= 2000 and amount <= 5000:
    discount = amount * 10/100
else:
    discount = 0

final_bill = amount - discount

print("Discount =", discount)
print("Final Bill =", final_bill)