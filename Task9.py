# Level 1: Beginner (if Statement)
# 1. Office Entry System
# Story:
# A company allows employees to enter only if they have a valid ID card.
# Question:
# Write a program that asks whether the employee has an ID card (yes/no).
# If yes, print:
# "Access Granted"
# Otherwise, do nothing.

Answer = input("Enter your Answer :")
print("Answer is :", Answer)

if Answer == "yes":
    print("Access Granted")
# ________________________________________

# 2. Movie Ticket
# A movie is only for people aged 18 or above.
# Take age as input.
# If eligible, print:
# You can watch the movie.

age = int(input("Enter your age :"))
print("Your age is :",age)

if age > 18:
    print("You can watch the movie")
# ________________________________________

# 3. Online Shopping
# Amazon gives free delivery only if the order amount is above ₹999.
# Take order amount.
# If eligible, print:
# Free Delivery Applied

Amount = int(input("Enter your order amount :"))
print("Your order amount is :",Amount)

if Amount > 999:
    print("Free Delivery Applied")
# ________________________________________

# 4. College Attendance
# A student can write the exam only if attendance is 75% or above.
# Take attendance percentage.
# Print:
# Eligible for Exam

Attendance = int(input("Enter your Attendance :"))
print("Your Attendance is : ",Attendance)

if Attendance >= 75:
    print("Eligible for Exam")
# ________________________________________

# 5. Gym Membership
# Only members can enter the gym.
# Ask:
# Are you a member?
# If yes, allow entry.

Answer = input("Enter your Answer : ")
print("Answer is :",Answer)

if Answer == "yes":
    print("Allow Entry")
# ________________________________________

# Level 2: if-else
# 6. Bank ATM
# Story
# A customer wants to withdraw money.
# Ask:
# •	Account Balance 
# •	Withdrawal Amount 
# If balance is sufficient
# Transaction Successful
# Else
# Insufficient Balance

Account_Balance = input("Enter your Account Balance :")
print("Account Balance is :",Account_Balance)

Withdrawal_Amount = input("Enter your Withdrawal Amount :")
print("Withdrawal Amount is :",Withdrawal_Amount)

if Account_Balance >= Withdrawal_Amount:
    print("Transaction Successful")
else:
    print("Insufficient Balance")
# _______________________________________

# 7. Password Verification
# Take password from the user.
# Correct password:
# Python@123
# If correct
# Login Successful
# Else
# Invalid Password

password = "Python@123"

Pass = input("Enter your Password :")

if Pass == password:
    print("Login Successful")
else:
    print("Invalid Password")
# ________________________________________

# 8. Restaurant Bill
# If bill amount is more than ₹500
# Apply 10% discount
# Otherwise
# No discount.

Amount = int(input("Enter your Bill Amount :"))
print("Bill Amount is :",Amount)

if Amount >= 500:
    print("Apply 10% discount")
else:
    print("No discount")
# ________________________________________

# 9. Cricket Stadium
# Only people having tickets can enter.
# Input:
# Do you have ticket?
# Display appropriate message.

print(f"Do you have ticket?")
Answer = input("Enter your Answer :")
print("Answer is :",Answer)

if Answer == "yes":
    print("You can enter in Hall")
else:
    print("You can not enter in Hall")
# ________________________________________

# 10. Petrol Pump
# A customer wants petrol worth ₹2000.
# If wallet balance is enough
# Fill petrol
# Else
# Transaction Failed

Amount = int(input("Enter your wallet balance :"))
print("wallet balance is :",Amount)

if Amount >= 2000:
    print("Fill petrol")
else:
    print("Transaction Failed")
# ________________________________________

# Level 3: if-elif-else
# 11. Student Grade System
# Marks:
# 90+
# Grade A
# 80+
# Grade B
# 70+
# Grade C
# Else
# Fail

Marks = int(input("Enter your Marks :"))
print("Marks is :",Marks)

if Marks > 0 and Marks <= 100:
    if Marks > 90 and Marks <= 100:
        print("Grade A")
    elif Marks >= 80 and Marks <= 90:
        print("Grade B")
    elif Marks >= 70 and Marks <= 80:
        print("Grade C")
    else:
        print("Fail")
else:
    print("Enter a Valid Marks")
# ________________________________________

# 12. Electricity Bill
# Monthly Units
# 0-100
# No charge
# 101-300
# ₹5/unit
# 301-500
# ₹8/unit
# Above 500
# ₹10/unit

Bill = int(input("Enter your Electricity Bill :"))
print("Electricity Bill is :",Bill)

if Bill > 0 and Bill <= 100:
    print("No charge")
elif Bill >= 101 and Bill <= 300:
    print("₹5/unit")
elif Bill >= 301 and Bill <= 500:
    print("₹8/unit")
else:
    print("₹10/unit")
# ________________________________________

# 13. Employee Bonus
# Experience
# Less than 2 years
# No Bonus
# 2-5 years
# ₹10,000
# 5-10 years
# ₹25,000
# More than 10
# ₹50,000

Experience = int(input("Enter your Experience :"))
print("Experience is :",Experience)

if Experience < 2:
    print("No Bonus")
elif Experience >= 2 and Experience < 5:
    print("Bonus Amount is ₹10,000")
elif Experience >= 5 and Experience < 10:
    print("Bonus Amount is ₹20,000")
else:
    print("Bonus Amount is ₹50,000")
# ________________________________________

# 14. Income Tax
# Income
# Less than ₹5L
# No Tax
# ₹5L-10L
# 10%
# ₹10L-20L
# 20%
# Above ₹20L
# 30%

Tax = int(input("Enter your Income Tax :"))
print("Income Tax is :L",Tax)

if Tax < 5:
    print("No Tax")
elif Tax > 5 and Tax <= 10:
    print("Income Tax is 10%")
elif Tax <= 20 and Tax > 10:
    print("Income Tax is 20%")
else:
    print("Income Tax is 30%")
# ________________________________________

# 15. Mobile Recharge
# Recharge Amount
# ₹99
# Basic Pack
# ₹199
# Standard
# ₹399
# Premium
# Otherwise
# Invalid Recharge

Recharge = int(input("Enter your Recharge Amount :"))
print("Recharge Amount is :",Recharge)

if Recharge == 99:
    print("Basic Pack")
elif Recharge == 199:
    print("Standard")
elif Recharge == 399:
    print("Premium")
else:
    print("Invalid Recharge")
# ________________________________________

# Level 4: Nested if
# 16. Company Interview
# Candidate must satisfy
# Age >=21
# AND
# Degree = BE/BTech
# Then eligible.
# Else not eligible.

Candidate_name = input("Enter your name :")
print("Candidate name is :",Candidate_name)

Degree = input("Enter your Degree :")
print("Candidate Degree is :",Degree)

Age = int(input("Enter your age :"))
print("Age is :",Age)

if Age >= 21:
    if Degree == "BE" or Degree == "BTech":
        print("Then eligible.")
    else:
        print("Not eligible.")
else:
    print("Enter Valid input")
# ________________________________________

# 17. Bank Loan
# Conditions
# Salary > ₹40,000
# AND
# Credit Score >700
# Loan Approved
# Else
# Rejected

Salary = int(input("Enter your Salary : "))
print("Customer Salary is :",Salary)

Score = int(input("Enter your Credit Score : "))
print("Customer Credit Score is :",Score)

if Salary > 40000:
    if Score > 700:
        print("Loan Approved")
    else:
        print("Rejected.")
else:
    print("Enter Valid input")
# ________________________________________

# 18. School Admission
# Student should
# Age >=5
# If yes
# Check documents
# If documents available
# Admission Confirmed
# Else
# Bring Documents

Age = int(input("Enter your age :"))
print("Age is :",Age)

Documents = input("Is your Documents available now : ")
print("Documents is :",Documents)

if Age >= 5:
    if Documents == "Yes":
        print("Admission Confirmed")
    else:
        print("Bring Documents.")
else:
    print("Enter Valid input")
# ________________________________________

# 19. Flight Boarding
# Passenger has ticket?
# If yes
# Passport verified?
# If yes
# Board Flight
# Else
# Verification Failed

ticket = input("If you have ticket : ")
print("ticket is :",ticket)

Passport = input("If you have Passport : ")
print("Passport is :",Passport)

if ticket == "yes":
    if Passport == "yes":
        print("Board Flight")
    else:
        print("Verification Failed")
else:
    print("Enter Valid input")
# ________________________________________

# 20. Online Exam
# Student Login
# If username correct
# Check password
# If password correct
# Start Exam
# Else
# Wrong Password

username = input("Enter your username : ")
print("Username is :",username)

password = input("Enter your password : ")
print("password is :",password)

if username == Snehal:
    if Passport == Snehal@1234:
        print("Start Exam")
    else:
        print("Wrong Password")
else:
    print("Enter Valid input")
# ________________________________________

# Level 5: Real-Time Business Scenarios
# 21. Food Delivery
# If restaurant is open
# Check delivery partner availability
# If available
# Order Accepted
# Else
# No Delivery Partner
# Else
# Restaurant Closed

Question1 = input("Is restaurant open now? : ")

Question2 = input("Is delivery partner available now? : ")

if Question1 == "Yes":
    if Question2 == "Yes":
        print("Order Accepted")
    else:
        print("No Delivery Partner")
else:
    print("Restaurant Closed")
# ________________________________________

# 22. Hospital Appointment
# Doctor Available?
# If yes
# Patient registered?
# If yes
# Appointment Confirmed
# Else
# Register First

Question1 = input("Is Doctor Available now? : ")

Question2 = input("Is Patient registered? : ")

if Question1 == "yes":
    if Question2 == "yes":
        print("Appointment Confirmed")
    else:
        print("Register First")

# ________________________________________

# 23. Railway Reservation
# Seats Available?
# If yes
# Book Ticket
# Else
# Waiting List

Question1 = input("Is Seats Available now? : ")

if Question1 == "yes":
    print("Book Ticket")
else:
    print("Waiting List")
# ________________________________________

# 24. Hotel Booking
# Room Available?
# If yes
# Advance Payment Done?
# If yes
# Booking Confirmed
# Else
# Pay Advance

Question1 = input("Is Room Available now? : ")

Question2 = input("Is Advance Payment Done? : ")

if Question1 == "yes":
    if Question2 == "yes":
        print("Booking Confirmed")
    else:
        print("Pay Advance")
# ________________________________________

# 25. Laptop Purchase
# Budget
# Below ₹40,000
# Basic Laptop
# ₹40,000-70,000
# Mid-range
# Above ₹70,000
# Gaming Laptop

Budget = int(input("Enter your Budget :"))
print("Budget is :",Budget)

if Budget < 40000:
    print("Basic Laptop")
elif Budget > 40000 and Budget <= 70000:
    print("Mid-range")
else:
    print("Gaming Laptop")
# ________________________________________

# Level 6: MNC Interview Logical Scenarios
# 26. Salary Hike
# Employee Rating
# 5
# 30% hike
# 4
# 20%
# 3
# 10%
# Below 3
# No hike

Rating = int(input("Enter your Rating :"))
print("Rating is :",Rating)

if Rating == 5:
    print("30% hike")
elif Rating == 4:
    print("20% hike")
elif Rating == 3:
    print("10% hike")
else:
    print("No hike")
# ________________________________________

# 27. Software License
# If license active
# Check expiry date
# If expired
# Renew License
# Else
# Software Opens

question1 = input("Is your license active now? : ")

date = input("Enter your expiry date : ")
print("Expiry date is :",date)

if date >= "25/06/2028" :
    print("Renew License")
else:
    print("Software Opens")
# ________________________________________

# 28. E-commerce Coupon
# Order Amount > ₹5000
# AND
# Coupon Available
# Apply 20%
# Otherwise
# No Discount

Coupon = input("Is Coupon Available now? : ")

amount = int(input("Enter your Amount : "))
print("Amount is :",amount)

if amount > 5000 and Coupon == "yes" :
    print("Apply 20%")
else:
    print("No Discount")
# ________________________________________

# 29. Hospital Emergency

# Patient Condition
# Critical
# Immediate ICU
# Serious
# Emergency Ward
# Normal
# General Ward

condition = input("Enter Patient Condition :")
print("Patient Condition is :",condition)

if condition == "Critical":
    print("Immediate ICU")
elif condition == "Serious":
    print("Emergency Ward")
elif condition == "Normal":
    print("General Ward")
else:
    print("Patient condition is normal")
# ________________________________________

# 30. Airport Security (Story-Based)
# Story
# Rahul reaches the airport for an international flight.
# Security follows these rules:
# •	Passenger must have a valid ticket. 
# •	Passport must be valid. 
# •	Visa must be valid. 
# •	Baggage weight must not exceed 30 kg. 
# If all conditions are satisfied:
# Boarding Allowed
# Otherwise, print the appropriate reason, such as:
# •	Ticket Missing 
# •	Passport Invalid 
# •	Visa Invalid 
# •	Excess Baggage 

ticket = input("Do you have a valid ticket? : ")
passport = input("Is your passport valid? : ")
visa = input("Is your visa valid? :")
baggage = float(input("Enter baggage weight in kg : "))
print("Baggage weight is :",baggage)

if ticket != "yes":
    print("Ticket Missing")
elif passport != "yes":
    print("Passport Invalid")
elif visa != "yes":
    print("Visa Invalid")
elif baggage > 30:
    print("Excess Baggage")
else:
    print("Boarding Allowed")
# ________________________________________

# Bonus Challenge (Real MNC Scenario)
# Online Banking Login
# Story
# A customer wants to transfer ₹50,000.
# The bank checks the following conditions:
# 1.	Username should be correct. 
# 2.	Password should be correct. 
# 3.	OTP should be correct. 
# 4.	Account balance should be greater than transfer amount. 
# 5.	Daily transfer limit should not exceed ₹1,00,000. 
# If every condition is satisfied:
# Transaction Successful
# Otherwise, display the first appropriate error message.

username = "rahul"
password = "pass123"
otp = "123456"
transfer_amount = 50000

username1 = input("Enter Username: ")
password1 = input("Enter Password: ")
otp1 = input("Enter OTP: ")
balance = float(input("Enter Account Balance: "))
daily_transfer = float(input("Enter Today's Transfer Amount: "))

# Validation
if username != username1:
    print("Invalid Username")
elif password != password1:
    print("Invalid Password")
elif otp != otp1:
    print("Invalid OTP")
elif balance < transfer_amount:
    print("Insufficient Balance")
elif daily_transfer + transfer_amount > 100000:
    print("Daily Transfer Limit Exceeded")
else:
    print("Transaction Successful")