# Question 1 — Banking ATM PIN Verification
# A customer visits an ATM to withdraw money.
# Business Context
# Banks allow only limited attempts to enter the correct PIN.
# Problem Statement
# Ask the user to enter a 4-digit PIN repeatedly until the correct PIN is entered or 3 attempts are exhausted.
# Required Inputs
# •	PIN entered by user 
# Expected Output
# •	Successful login 
# •	OR account temporarily blocked 
# Constraints
# •	Maximum 3 attempts 
# •	Use only loops and conditions 
# Learning Objective
# Using while loop with counting.
# Real-world Application
# ATM authentication systems.

c_pin = "1234"
attempts = 0

while attempts < 3:
    pin = input("Enter your 4-digit PIN : ")

    if pin == c_pin:
        print("Successful login")
        break
    else:
        attempts+=1
        print("Incorrect PIN")

if attempts == 3:
    print("Account temporarily blocked")
# ________________________________________


# Question 2 — Hospital Temperature Monitoring
# A nurse records patient temperature every hour.
# Business Context
# The monitoring continues until the doctor stops it.
# Problem Statement
# Keep accepting temperature values until the user enters -1.
# Required Inputs
# •	Temperature readings 
# Expected Output
# •	Total readings recorded 
# •	Average temperature 
# Constraints
# •	Ignore negative values except -1 
# Learning Objective
# Accumulation using loops.
# Real-world Application
# Patient monitoring software.

total = 0 
count = 0

while True:
    temp = float(input("Enter temperature -1 to stop :"))

    if temp == -1:
        break
    elif temp < 0:
        print("Invalid temperature")
    else:
        total = total + temp
        count = count + 1
if count > 0:
    Average = total/count
    print("Total reading recorded :",count)
    print("Average temperature :",Average)
else:
    print("No temperature readings recorded")
# ________________________________________


# Question 3 — Online Shopping Cart
# A customer keeps adding item prices into the shopping cart.
# Business Context
# Billing system calculates the total amount.
# Problem Statement
# Accept item prices until the customer enters 0.
# Required Inputs
# •	Item prices 
# Expected Output
# •	Total bill 
# •	Number of products 
# Constraints
# Prices must be positive.
# Learning Objective
# Counting and summation.
# Real-world Application
# E-commerce checkout systems.

total = 0 
count = 0

while True:
    price = float(input("Enter item price :"))

    if price == 0:
        break
    elif price < 0:
        print("Invalid price")
    else:
        total = total + price
        count = count + 1
print("Number of products:" ,count)
print("Total Bill : ",total)
# ________________________________________


# Question 4 — School Attendance
# A teacher marks attendance for students.
# Business Context
# The class has 40 students.
# Problem Statement
# Display roll numbers from 1 to 40.
# Required Inputs
# None
# Expected Output
# Attendance roll numbers
# Constraints
# Use for loop only.
# Learning Objective
# Using range().
# Real-world Application
# Attendance software.

for roll_no in range(1,41):
    print("Roll number : ",roll_no)
# ________________________________________


# Question 5 — Retail Discount Days
# A retail store announces discounts for 7 days.
# Business Context
# Marketing team needs daily announcements.
# Problem Statement
# Print "Discount Available Today" for seven consecutive days.
# Required Inputs
# None
# Expected Output
# Seven announcements
# Learning Objective
# Simple iteration.
# Real-world Application
# Retail promotions.

for day in range(1,8):
    print("Day",day,"- Discount Available Today")
# ________________________________________


# Question 6 — HR Employee ID Validation
# An HR executive enters employee IDs.
# Business Context
# Employee ID cannot be empty.
# Problem Statement
# Keep asking for Employee ID until a valid one is entered.
# Required Inputs
# Employee ID
# Expected Output
# Valid Employee ID accepted.
# Constraints
# Empty input is invalid.
# Learning Objective
# Input validation using loops.
# Real-world Application
# Employee onboarding.

id = ""

while id == "":
    id = input("Enter Employee ID : ")

    if id == "":
        print("Employee ID cannot be empty")

print("Valid Employee ID accepted")
# ________________________________________


# Question 7 — Telecom Recharge
# A customer repeatedly enters recharge amounts.
# Business Context
# Recharge continues until customer exits.
# Problem Statement
# Accept recharge amounts until 0 is entered.
# Required Inputs
# Recharge amount
# Expected Output
# Total recharge value
# Learning Objective
# Accumulation.
# Real-world Application
# Telecom billing.

total = 0

while True:
    amount = float(input("Enter recharge amount : "))

    if amount == 0:
        break
    elif amount < 0:
        print("Invalid recharge amount")
    else :
        total = total + amount
print("Total recharge value:", total)
# ________________________________________


# Question 8 — Travel Ticket Booking
# Passengers book tickets one after another.
# Business Context
# Bus capacity is 30 seats.
# Problem Statement
# Display seat numbers from 1 to 30.
# Required Inputs
# None
# Expected Output
# Seat allocation numbers.
# Learning Objective
# For loop.
# Real-world Application
# Reservation systems.

for seat in range(1, 31):
    print("Seat Number :", seat)
# ________________________________________


# Question 9 — Cybersecurity Login Attempts
# A user repeatedly enters passwords.
# Business Context
# Maximum five attempts.
# Problem Statement
# Stop accepting passwords once the correct password is entered.
# Required Inputs
# Password
# Expected Output
# Access Granted or Account Locked
# Learning Objective
# while loop + break.
# Real-world Application
# Authentication systems.

c_pass = "admin123"
attempts = 0

while attempts < 5:
    password = input("Enter password: ")

    if password == c_pass:
        print("Access Granted")
        break
    else:
        attempts = attempts + 1
        print("Incorrect Password")

if attempts == 5:
    print("Account Locked")
# ________________________________________


# Question 10 — Manufacturing Production Counter
# A machine produces products continuously.
# Business Context
# Supervisor enters production quantity every hour.
# Problem Statement
# Accept hourly production until shift ends.
# Required Inputs
# Production count
# Expected Output
# Total products manufactured.
# Learning Objective
# Counting.
# Real-world Application
# Factory monitoring.

total = 0

while True:
    production = int(input("Enter production count : "))

    if production == 0:
        break
    elif production < 0:
        print("Invalid production count")
    else:
        total = total + production

print("Total products manufactured:", total)
# ________________________________________


# Question 11 — Banking Loan EMI Collection
# A bank collects monthly EMI payments.
# Business Context
# Payment continues until the entire loan is cleared.
# Problem Statement
# Accept monthly payments until the remaining loan amount becomes zero.
# Required Inputs
# •	Loan amount 
# •	Monthly payment 
# Expected Output
# Remaining balance after every payment and loan closure message.
# Constraints
# Payment cannot exceed the remaining balance.
# Learning Objective
# while loop with accumulation.
# Real-world Application
# Loan management systems.

amount = float(input("Enter loan amount: "))
remaining = amount

while remaining > 0:
    payment = float(input("Enter monthly payment: "))

    if payment <= 0:
        print("Invalid payment")
        continue

    if payment > remaining:
        print("Payment cannot exceed remaining balance:", remaining)
        continue

    remaining = remaining - payment
    print("Remaining balance:", remaining)

print("Loan fully cleared. Congratulations!")
# ________________________________________


# Question 12 — Healthcare Patient Queue
# Patients are examined one by one.
# Business Context
# The clinic serves 25 patients daily.
# Problem Statement
# Display patient token numbers from 1 to 25. Skip token 13 because the patient canceled.
# Required Inputs
# None
# Expected Output
# Patient tokens excluding 13.
# Constraints
# Use continue.
# Learning Objective
# Loop control using continue.
# Real-world Application
# Hospital queue management.

for token in range(1,26):

    if token == 13:
        continue 

    print("Patient Token:", token)
# ________________________________________


# Question 13 — E-Commerce Flash Sale
# A flash sale has only 100 products in stock.
# Business Context
# Orders are accepted until stock becomes zero.
# Problem Statement
# Keep accepting order quantities until stock is exhausted.
# Required Inputs
# Order quantity
# Expected Output
# Remaining stock after every order.
# Constraints
# Orders exceeding stock should be rejected.
# Learning Objective
# while loop with validation.
# Real-world Application
# Inventory systems.

stock = 100

while stock > 0:
    order = int(input("Enter order quantity: "))

    if order <= 0:
        print("Invalid order quantity")
        continue

    if order > stock:
        print("Order rejected Only", stock, "items left in stock.")
        continue

    stock = stock - order
    print("Remaining stock:", stock)

print("Stock exhausted. Flash sale ended.")
# ________________________________________


# Question 14 — Education Online Examination
# Students answer 20 questions.
# Business Context
# The exam ends immediately if the student quits.
# Problem Statement
# Ask whether the student wants to continue after each question. Stop if they choose to quit.
# Required Inputs
# Continue response
# Expected Output
# Exam completed or terminated.
# Constraints
# Use break.
# Learning Objective
# Loop termination.
# Real-world Application
# Online examination systems.

for question in range(1,21):
    print("Question", question)

    choice = input("Do you want to continue? : ")

    if choice.lower() == "no":
        print("Exam terminated by student.")
        break

else:
    print("Exam completed successfully.")
# ________________________________________


# Question 15 — HR Salary Processing
# Payroll processes salaries for 50 employees.
# Business Context
# The HR department wants to skip employees on unpaid leave.
# Problem Statement
# Display salary processing messages while skipping unpaid leave employee IDs.
# Required Inputs
# Leave status
# Expected Output
# Salary processed or skipped.
# Constraints
# Use continue.
# Learning Objective
# Loop control.
# Real-world Application
# Payroll software.

for id in range(1, 51):

    status = input("Employee " + str(id) + " on leave? : ")

    if status.lower() == "yes":
        print("Employee", id, "- Salary skipped unpaid leave")
        continue

    print("Employee", id, "- Salary processed")
# ________________________________________


# Question 16 — Logistics Package Scanning
# A warehouse scans packages before dispatch.
# Business Context
# A damaged package should stop the dispatch process.
# Problem Statement
# Accept package status until a damaged package is found.
# Required Inputs
# Package condition
# Expected Output
# Dispatch continues or stops.
# Constraints
# Use break.
# Learning Objective
# Conditional loop termination.
# Real-world Application
# Warehouse automation.

while True:
    status = input("Enter package status good/damaged: ")

    if status.lower() == "damaged":
        print("Damaged package found Dispatch stopped.")
        break

    print("Package scanned. Dispatch continues.")
# ________________________________________


# Question 17 — Retail Billing Counter
# Cashier scans products one by one.
# Business Context
# The customer finishes shopping by entering a sentinel value.
# Problem Statement
# Accept product prices until checkout is completed.
# Required Inputs
# Product price
# Expected Output
# Total bill and item count.
# Constraints
# Sentinel value ends input.
# Learning Objective
# Accumulation using loops.
# Real-world Application
# POS billing systems.

total = 0
count = 0

while True:
    price = float(input("Enter product price : "))

    if price == 0:
        break
    elif price < 0:
        print("Invalid price")
        continue

    total = total + price
    count = count + 1

print("Total items:", count)
print("Total bill:", total)
# ________________________________________


# Question 18 — Government Tax Collection
# Citizens submit tax payments.
# Business Context
# The office records payments until the working day ends.
# Problem Statement
# Accept tax amounts until the operator ends the session.
# Required Inputs
# Tax amount
# Expected Output
# Total tax collected.
# Learning Objective
# Accumulation.
# Real-world Application
# Revenue management systems.

total_tax = 0

while True:
    tax = float(input("Enter tax amount : "))

    if tax == 0:
        break
    elif tax < 0:
        print("Invalid tax amount")
        continue

    total_tax = total_tax + tax

print("Total tax collected:", total_tax)
# ________________________________________


# Question 19 — Social Media Comment Moderation
# Moderators review comments.
# Business Context
# Comments containing banned words are ignored.
# Problem Statement
# Process comments until "END" is entered.
# Required Inputs
# Comment text
# Expected Output
# Accepted or skipped comments.
# Constraints
# Use continue.
# Learning Objective
# Filtering using loops.
# Real-world Application
# Content moderation.

banned_word = []
accepted_word = []

while True:
    comment = input("Enter a comment : ")

    if comment == "end".lower():
        break

    if comment in ["spam","block","fraud"]:
        banned_word.append(comment)
        print(f"Banned words : {comment}")
        continue
    else:
        accepted_word.append(comment)
        # print(f"comment Accepted : {comment}")

print(f"Banned comment : {banned_word}")
print(f"Accepted comment: {accepted_word}")

# ________________________________________

# Question 20 — Software Installation Wizard
# Installation has multiple setup steps.
# Business Context
# Each step requires user confirmation.
# Problem Statement
# Repeat installation steps until all confirmations are completed.
# Required Inputs
# Confirmation
# Expected Output
# Installation completed.
# Constraints
# Restart current step if confirmation is invalid.
# Learning Objective
# Input validation.
# Real-world Application
# Desktop installers.

steps = 5 

for step in range(1,steps + 1):
    while True:
        print("Step",step, ": Installation in progress...")
        confirm = input("Confirm step completion (yes/no): ")

        if confirm.lower() == "yes":
            print("Step",step, "completed\n")
            break
        elif confirm.lower() == "no":
            print("Step",step, "restarted\n")
        else:
            print("Invalid input. Please enter yes or no.\n")

print("Installation completed successfully.")
# ________________________________________


# Question 21 — Manufacturing Quality Inspection
# Each production batch contains multiple products.
# Business Context
# Every product must be inspected.
# Problem Statement
# Display inspection progress for 10 batches, each containing 20 products.
# Required Inputs
# None
# Expected Output
# Batch number and product number.
# Constraints
# Use nested loops.
# Learning Objective
# Nested iteration.
# Real-world Application
# Quality assurance.

for batch in range(1,11): 
    print("Batch", batch)

    for product in range(1,21):  
        print("Inspecting Product",product)

    print()
# ________________________________________


# Question 22 — Banking Branch Transaction Report
# A bank has multiple branches.
# Business Context
# Each branch records daily transactions.
# Problem Statement
# Display transaction numbers for every branch.
# Required Inputs
# Number of branches
# Transactions per branch
# Expected Output
# Transaction sequence.
# Constraints
# Use nested loops.
# Learning Objective
# Nested loops with variable ranges.
# Real-world Application
# Core banking.

branches = int(input("Enter number of branches: "))

for branch in range(1, branches + 1):
    print("Branch", branch)

    transactions = int(input("Enter number of transactions: "))

    for t in range(1, transactions + 1):
        print("  Transaction", t)

    print()

# ________________________________________


# Question 23 — Airline Seat Reservation
# An aircraft has rows and seats.
# Business Context
# Reservation system shows all seats.
# Problem Statement
# Display seat layout using nested loops.
# Required Inputs
# Rows
# Seats per row
# Expected Output
# Seat identifiers.
# Constraints
# Nested loops only.
# Learning Objective
# 2-dimensional iteration.
# Real-world Application
# Airline booking.

rows = int(input("Enter number of rows: "))
seats_per_row = int(input("Enter seats per row: "))

for row in range(1, rows + 1):
    for seat in range(1,seats_per_row + 1):
        print("R" + str(row) + "S" + str(seat), end=" ")
    print()
# ________________________________________


# Question 24 — Cybersecurity Port Scanner Simulation
# A security engineer scans ports.
# Business Context
# Scanning stops when an open vulnerable port is detected.
# Problem Statement
# Scan ports within a given range and stop immediately when a vulnerable port is encountered.
# Required Inputs
# Starting port
# Ending port
# Vulnerable port
# Expected Output
# Scanned ports and stopping message.
# Constraints
# Use break.
# Learning Objective
# Early loop termination.
# Real-world Application
# Security auditing.

start = int(input("Enter starting port: "))
end = int(input("Enter ending port: "))
vulnerable_port = int(input("Enter vulnerable port: "))

for port in range(start, end + 1):

    print("Scanning port:", port)

    if port == vulnerable_port:
        print("Vulnerable port found! Stopping scan.")
        break

print("Scan completed.")
# ________________________________________


# Question 25 — Telecom Call Center
# Customer support operates continuously.
# Business Context
# The system runs indefinitely until the supervisor shuts it down.
# Problem Statement
# Create a menu-driven customer support system that repeats until Exit is selected.
# Required Inputs
# Menu choice
# Expected Output
# Selected operation or exit message.
# Constraints
# Use an infinite loop.
# Learning Objective
# Infinite loops and menu-driven programming.
# Real-world Application
# Call center software.

while True:
    print("\n--- Customer Support Menu ---")
    print("1. Check Balance")
    print("2. Recharge Account")
    print("3. Talk to Agent")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is being checked...")

    elif choice == "2":
        print("Recharge option selected...")

    elif choice == "3":
        print("Connecting to an agent...")

    elif choice == "4":
        print("Exiting system. Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
# ________________________________________


# Question 26 — Government Citizen Service Portal
# Citizens access multiple services.
# Business Context
# Portal remains active throughout office hours.
# Problem Statement
# Implement a menu-driven application for repeated service selection until logout.
# Required Inputs
# Service option
# Expected Output
# Requested service or logout.
# Constraints
# Use while True.
# Learning Objective
# Menu-driven applications.
# Real-world Application
# Government portals.

while True:
    print("\n--- Citizen Service Portal ---")
    print("1. Apply for ID Card")
    print("2. Pay Utility Bill")
    print("3. Request Certificate")
    print("4. Check Application Status")
    print("5. Logout")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("ID Card application initiated...")

    elif choice == "2":
        print("Utility bill payment portal opened...")

    elif choice == "3":
        print("Certificate request submitted...")

    elif choice == "4":
        print("Fetching application status...")

    elif choice == "5":
        print("Logged out successfully. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
# ________________________________________


# Question 27 — Software Build Verification
# A DevOps engineer validates build stages.
# Business Context
# Every stage must pass before deployment.
# Problem Statement
# Iterate through build stages. If all stages complete successfully, display a deployment-ready message using a loop else block.
# Required Inputs
# Stage status
# Expected Output
# Deployment ready or build failed.
# Constraints
# Use loop with else.
# Learning Objective
# Understanding loop else.
# Real-world Application
# CI/CD pipelines.

stages = [True, True, True, True] 

for stage in stages:
    if not stage:
        print("Build failed")
        break
else:
    print("Deployment ready")
# ________________________________________


# Question 28 — Banking Fraud Detection Console
# Story / Scenario
# A fraud analyst monitors live transactions.
# Business Context
# Transactions are continuously received until a suspicious transaction exceeds a predefined risk threshold.
# Problem Statement
# Process incoming transaction risk scores. Ignore invalid scores, stop immediately when a fraudulent score is detected, and display the total number of valid transactions analyzed before termination.
# Required Inputs
# •	Risk score for each transaction 
# •	Fraud threshold 
# Expected Output
# •	Valid transactions processed 
# •	Fraud detection message 
# •	Monitoring stopped 
# Constraints
# •	Use an infinite loop 
# •	Use continue for invalid scores 
# •	Use break when fraud is detected 
# Learning Objective
# Combining infinite loops, continue, break, and counting.
# Real-world Application
# Real-time fraud monitoring.

fraud_threshold = 80  
valid_transactions = 0

while True:
    score_input = input("Enter transaction risk score (or 'exit' to stop): ")

    if score_input.lower() == "exit":
        break

    if not score_input.isdigit():
        print("Invalid score ignored")
        continue

    score = int(score_input)

    if score < 0 or score > 100:
        print("Invalid score ignored")
        continue

    valid_transactions += 1

    if score > fraud_threshold:
        print("Fraud detected")
        break

    print("Transaction is safe")

print("\nMonitoring stopped")
print("Valid transactions processed:", valid_transactions)
# ________________________________________


# Question 29 — Smart Warehouse Order Fulfillment
# A warehouse processes orders across multiple storage zones.
# Business Context
# Each zone contains several shelves, and each shelf contains multiple packages.
# Problem Statement
# Iterate through zones and shelves to simulate package picking. If a damaged package is encountered, skip it. If an emergency stop signal is received, terminate all processing immediately.
# Required Inputs
# •	Number of zones 
# •	Shelves per zone 
# •	Package status 
# •	Emergency stop signal 
# Expected Output
# •	Packages picked 
# •	Damaged packages skipped 
# •	Emergency shutdown message (if applicable) 
# Constraints
# •	Use nested loops 
# •	Use continue for damaged packages 
# •	Use break to stop processing 
# Learning Objective
# Advanced nested-loop control and business process simulation.
# Real-world Application
# Warehouse Management Systems (WMS).

zones = int(input("Enter number of zones: "))
shelves_per_zone = int(input("Enter shelves per zone: "))

for zone in range(1, zones + 1):
    print(f"\nProcessing Zone {zone}")

    for shelf in range(1, shelves_per_zone + 1):
        print(f"  Shelf {shelf}")

        packages = int(input("    Enter number of packages: "))

        for p in range(1, packages + 1):
            status = input(f"      Package {p} status (good/damaged/stop): ").lower()

            if status == "stop":
                print("\n Emergency stop received! Shutting down warehouse processing...")
                break

            if status == "damaged":
                print(" Damaged package skipped")
                continue

            print(" Package picked")

        else:
            continue

        break

    else:
        continue

    break

print("\nWarehouse processing completed")
# ________________________________________
# Question 30 — Multi-Department Enterprise Management Console
# A multinational company operates Banking, HR, Finance, Retail, Logistics, and Customer Support departments through a unified console.
# Business Context
# An operations manager performs repetitive tasks for different departments throughout the day.
# Problem Statement
# Design a menu-driven program that repeatedly displays department options and executes the selected operation. The application should continue until the manager chooses to exit. Invalid menu selections must be rejected, canceled operations should return to the menu, and successful completion of all scheduled operations should display a final completion message.
# Required Inputs
# •	Department selection 
# •	Operation choice 
# •	Continue/Exit option 
# Expected Output
# •	Department menu displayed repeatedly 
# •	Selected operation processed 
# •	Invalid selections handled 
# •	System exits only when requested 
# •	Final completion message after successful workflow 
# Constraints
# •	Use while True 
# •	Use break, continue, and pass where appropriate 
# •	Use input validation with loops 
# •	Do not use functions, collections, classes, exception handling, or modules

while True:
    print("\n===== Enterprise Management Console =====")
    print("1. Banking")
    print("2. HR")
    print("3. Finance")
    print("4. Retail")
    print("5. Logistics")
    print("6. Customer Support")
    print("7. Exit")

    choice = input("Select a department (1-7): ")

    if choice == "7":
        print("System exit requested...")
        break

    if choice == "1":
        print("Banking department selected ✔")
        op = input("Enter operation (deposit/withdraw): ")

        if op == "deposit":
            print("Processing deposit...")
        elif op == "withdraw":
            print("Processing withdrawal...")
        else:
            print("Invalid operation ")
            continue

    elif choice == "2":
        print("HR department selected ✔")
        op = input("Enter operation (hire/payroll): ")

        if op == "hire":
            print("Processing hiring...")
        elif op == "payroll":
            print("Processing payroll...")
        else:
            print("Invalid operation ")
            continue

    elif choice == "3":
        print("Finance department selected ✔")
        op = input("Enter operation (budget/audit): ")

        if op == "budget":
            print("Processing budget...")
        elif op == "audit":
            print("Processing audit...")
        else:
            print("Invalid operation ")
            continue

    elif choice == "4":
        print("Retail department selected ✔")
        op = input("Enter operation (sales/inventory): ")

        if op == "sales":
            print("Processing sales...")
        elif op == "inventory":
            print("Processing inventory...")
        else:
            print("Invalid operation")
            continue

    elif choice == "5":
        print("Logistics department selected ✔")
        op = input("Enter operation (shipping/tracking): ")

        if op == "shipping":
            print("Processing shipping...")
        elif op == "tracking":
            print("Processing tracking...")
        else:
            print("Invalid operation ")
            continue

    elif choice == "6":
        print("Customer Support selected ")
        op = input("Enter operation (ticket/call): ")

        if op == "ticket":
            print("Creating support ticket...")
        elif op == "call":
            print("Initiating customer call...")
        else:
            print("Invalid operation")
            continue

    else:
        print("Invalid department selection")
        pass

print("\nAll requested operations completed successfully")