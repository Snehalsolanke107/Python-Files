
# Task 1: Employee Salary Management System
# An IT company wants to store employee details temporarily before saving 
# them to the database.

employee_id = 101
employee_name = "Rahul"
employee_salary = 50000
employee_department = "Python"

print(f"""     
 ----- EMPLOYEE DETAILS -----
       Employee ID :{employee_id}
       Employee Name :{employee_name}
       Salary :{employee_salary}
       Department :{employee_department}
""")

# Task 2: E-Commerce Product Information
# Amazon wants to display product information.

product_id = 51
product_name = "Machine"
product_price = 500
product_stock = 100

print(f"""         
 ----- AMAZON STORE DETAILS -----
       Product ID :{product_id}
       Product Name :{product_name}
       Product Price :{product_price}
       Product Stock :{product_stock}
""")

# Task 3: Banking Application
# Create valid identifiers for:

account_number = 12345678
customer_name = "Snehal"
account_balance = 50000

print(f"""         
 ----- BANK ACCOUNT DETAILS -----
       Account Number :{account_number}
       Customer Name :{customer_name}
       Account Balance :{account_balance}
""")

# Also Identify Invalid Identifiers 
1name = name1
class = Class1
first-name = first_name

# Task 4: Login Authentication System
# A developer accidentally uses keywords as variable names.
# Find the errors.

class = "Python" # SyntaxError: invalid syntax
for = 10 # SyntaxError: invalid syntax
if = "Admin" # SyntaxError: invalid syntax

Language = "Python"
Count = 10
User = "Admin"

print(f"""
----- LOGIN SYSTEM DETAILS -----
      Language is :{Language}
      Count of :{Count}
      User is :{User}
""")

# Task 5: Online Movie Ticket Booking
# BookMyShow stores the number of tickets booked.

Tickets = 5
ticket_price = 250

Total = Tickets * ticket_price

print(f"""
----- BOOKMYSHOW STORES DETAILS -----
      Tickets Count :{Tickets}
      Ticket Price :{ticket_price}
      Total Amount is :{Total}
""")

# Task 6: Warehouse Inventory
# A warehouse has 500 items.
# 100 items sold.
# Calculate remaining stock.

Total_items = 500
Sold_items = 100

Remaining_items = Total_items - Sold_items

print(f"""
----- Warehouse Inventory -----
      Total items is :{Total_items}
      Total items is :{Sold_items}
      Remaining items is :{Remaining_items}
""")

# Task 7: Petrol Pump Billing
# A customer purchases 12.5 liters of petrol.
# Price per liter: 105.50

Price_per_liter = 105.50
purchases_petrol = 12.5
Total_Bill = Price_per_liter *purchases_petrol

print(f"""
----- Petrol Pump Billing -----
      Price of per liter :{Price_per_liter}
      Total Purchases petrol :{purchases_petrol}
      Total Bill is :{Total_Bill}
""") 

# Task 8: Student Percentage Calculator
# Calculate percentage of student marks.

obtained = 455
total = 500

Percentage = (obtained / total) * 100

print(f"""
----- Student Percentage Calculator -----
      Obtained Marks :{obtained}
      Total Marks :{total}
      Percentage is :{Percentage}
""")

# Task 9: Electrical Engineering Application
# An engineering company uses complex numbers for AC circuit 

voltage = 220 + 50j
current = 10 + 5j

print(f"""
----- Electrical Engineering Application -----
      Voltage is :{voltage}
      Current is :{current}
      Datatype of Voltage :,{type(voltage)}
      Datatype of Current :,{type(current)}
""")

# Task 10: Signal Processing System
# Store two complex signals.

signal1 = 5 + 3j
signal2 = 2 + 7j

# Output

print(f"""
----- Signal Processing System -----
      Signal1 is :{signal1}
      Signal2 is :{signal2}
      Addition is :{signal1+signal2}
""")

# Task 11: Online Shopping Discount System
# Price is received as String from API.

price = "2500"
print(type(price))
discount = 10

# Convert into integer and apply discount and calculate total price.
price = int(price)
print(type(price))

Discount = 2500*10/100
print(f"""
----- Online Shopping Discount -----
      Price is :{price}
      Discount is :{discount}
      Discount is :{Discount}
""")

# Task 12: ATM Withdrawal System
# Amount entered from keyboard.

amount = "5000"
print(type(amount))

# Convert into float.

amount = float(amount)
print(type(amount))

print(f"""
----- ATM Withdrawal System -----
      Withdrawal Amount is :{amount}
""")

# Task 13: Sensor Monitoring System
# Temperature received:

temp = 35.89
print("Tempture is :",temp)
print(type(temp))
# Output:
# 35
temp = int(temp)
print("Tempture converts into int :",temp)
print(type(temp))

# Task 14: Student Registration Form
# College website collects student details.
# Requirements 
# Take input:

name = input("Enter Name : ")
age = int(input("Enter Age : "))
course = input("Enter Course : ")

# Display information.

print(f"""
----- Student Registration Form Details -----
      Student name is :{name}
      Student age is :{age}
      Student course is :{course}
""")

# Task 15: Hospital Management System
# A hospital receptionist registers a patient.
# Requirements 
# Take:

Patient_ID = input("Enter Patient ID : ")
Patient_Name = input("Enter Patient Name : ")
Age = int(input("Enter Age : "))
Weight = float(input("Enter Weight : "))

# Store using variables.
# Display patient card.

print(f"""
----- Hospital Management System -----
      Patient ID is :{Patient_ID}
      Patient name is :{Patient_Name}
      Patient age is :{Age}
      Patient Weight is :{Weight}
""")

# Task 16: Food Delivery Application
# Zomato wants to generate order bills.
# Inputs 

Customer_Name = input("Enter Customer Name : ")
Food_Item = input("Enter Food Item : ")
Quantity = int(input("Enter Quantity : "))
Price = int(input("Enter Price : "))

# Calculate 
print(f"""
----- Zomato Bill -----
      Customer Name is :{Customer_Name}
      Food Item is :{Food_Item}
      Quantity is :{Quantity}
      Food Price is :{Price}
      Total Bill is : Rs {Quantity*Price} 
""")

# Task 17: Employee Payroll System
# An MNC generates monthly salaries.
# Inputs 

Employee_Name = input("Enter Employee Name : ")
Basic_Salary = float(input("Basic Salary : "))
Bonus = int(input("Enter Quantity : "))
Tax = int(input("Enter Quantity : "))

# Formula
print(f"""
----- Employee Payroll System -----
      Employee Name is :{Employee_Name}
      Basic Salary is :{Basic_Salary}
      Bonus is :{Bonus}
      Tax is :{Tax}
      Net Salary : Rs {Basic_Salary+Bonus-Tax} 
""")

# Task 18: Bank Account Opening System
# Create a mini banking registration portal.
# Inputs 
Account_Number = int(input("Enter Account Number : "))
Customer_Name = input("Enter Customer Name : ")
Initial_Deposit int(input("Enter Initial Deposit : "))

# Conditions 
# Store values using proper identifiers. 

print(f"""
----- Bank Account Opening System -----
      Account Number is :{Account_Number}
      Customer Name is :{Customer_Name}
      Initial Deposit is :{Initial_Deposit}
""")

# Task 19: Smart Electricity Bill Generator (MNC Level)
# An electricity company wants an automated bill generation system.
# Inputs 

customer_id = input("Enter Customer ID: ")
customer_name = input("Enter Customer Name: ")
units = float(input("Enter Units Consumed: "))
rate = float(input("Enter Rate Per Unit: "))

# Calculate 
# Bill Amount
# GST = 18%
# Final Bill
bill_amount = units * rate
gst = bill_amount * 18 / 100
final_bill = bill_amount + gst

print(f"""
----- Smart Electricity Bill Generator -----
      Customer ID is :{customer_id}
      Customer Name is :{customer_name}
      Units Consumed :{units}
      Rate Per Unit :{rate}
      Bill Amount is :{bill_amount}
      GST is :{gst}
      Final Bill Amount is :{final_bill}
""")

# Task 20: Online Course Enrollment Portal (Startup Interview Level)
# A training institute receives student details from a web form.
# Inputs 

student_id = int(input("Enter Student ID: "))
student_name = input("Enter Student Name: ")
course_name = input("Enter Course Name: ")
course_fee = float(input("Enter Course Fee: "))
gst_percentage = float(input("Enter GST Percentage: "))
# Calculate 

gst_amount = (course_fee * gst_percentage) / 100
total_fee = course_fee + gst_amount

# Challenge 
# Display datatype of every variable

print(f"""
----- Online Course Enrollment Portal -----
      Student ID is :{student_id}
      Datatype of Student ID :,{type(student_id)}
      Student Name is :{student_name}
      Datatype of Student Name :,{type(student_name)}
      Course Name is :{course_name}
      Datatype of Course Name :,{type(course_name)}
      Course Fee is :{course_fee}
      Datatype of Course Fee :,{type(course_fee)}
      GST Percentage is :{gst_percentage}
      Datatype of GST Percentage :,{type(gst_percentage)}
      GST Amount is :, {gst_amount}
      Datatype of GST Amount :,{type(gst_amount)}
      Total fees Amount is :, {total_fee}
      Datatype of Total fees Amount :,{type(total_fee)}
""")