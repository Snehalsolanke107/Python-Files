loans = {
    101: {
        "name": "Amit",
        "age": 28,
        "city": "Pune",
        "loan_amount": 500000,
        "interest_rate": 8.5,
        "loan_term": 5,
        "credit_score": 750,
        "status": "Approved"
    },
    102: {
        "name": "Priya",
        "age": 35,
        "city": "Mumbai",
        "loan_amount": 800000,
        "interest_rate": 9.2,
        "loan_term": 10,
        "credit_score": 680,
        "status": "Approved"
    },
    103: {
        "name": "Rahul",
        "age": 24,
        "city": "Pune",
        "loan_amount": 250000,
        "interest_rate": 10.5,
        "loan_term": 3,
        "credit_score": 590,
        "status": "Rejected"
    },
    104: {
        "name": "Sneha",
        "age": 42,
        "city": "Nashik",
        "loan_amount": 1000000,
        "interest_rate": 7.8,
        "loan_term": 15,
        "credit_score": 800,
        "status": "Approved"
    },
    105: {
        "name": "Vikas",
        "age": 31,
        "city": "Mumbai",
        "loan_amount": 450000,
        "interest_rate": 11.0,
        "loan_term": 5,
        "credit_score": 620,
        "status": "Pending"
    },
    106: {
        "name": "Neha",
        "age": 29,
        "city": "Pune",
        "loan_amount": 650000,
        "interest_rate": 8.9,
        "loan_term": 7,
        "credit_score": 720,
        "status": "Approved"
    },
    107: {
        "name": "Karan",
        "age": 45,
        "city": "Nagpur",
        "loan_amount": 1200000,
        "interest_rate": 9.5,
        "loan_term": 20,
        "credit_score": 650,
        "status": "Pending"
    },
    108: {
        "name": "Pooja",
        "age": 38,
        "city": "Nashik",
        "loan_amount": 300000,
        "interest_rate": 10.0,
        "loan_term": 4,
        "credit_score": 580,
        "status": "Rejected"
    },
    109: {
        "name": "Rohit",
        "age": 33,
        "city": "Mumbai",
        "loan_amount": 900000,
        "interest_rate": 8.2,
        "loan_term": 12,
        "credit_score": 770,
        "status": "Approved"
    },
    110: {
        "name": "Anjali",
        "age": 26,
        "city": "Nagpur",
        "loan_amount": 400000,
        "interest_rate": 9.8,
        "loan_term": 5,
        "credit_score": 690,
        "status": "Pending"
    }
}

# WAP To print all customer names.

for i in loans.values():
    print(i)
print(loans)


# WAP to print all customer name with loan amount

for i in loans.values():
    name = i["name"]
    Loan = i["loan_amount"]

    print(f"Name:{name} | Loan Amount : {Loan}")

# WAP to count total no. of customers without using len function
count = 0
for i in loans.items():
    count = count + 1
    print(count)

# WAP to input ID then show customer details
Loan_ID = int(input("Enter ID : "))
data = loans[Loan_ID]
for i,j in data.items():
    print(f"{i.title()} - {j}")

# WAP to input ID then show customer details and remove _ in key

Loan_ID = int(input("Enter ID : "))
data = loans[Loan_ID]
for i,j in data.items():
    print(f"{i.replace("_"," ")} - {j}")

Loan_details = {}
for i in loans.values():
    name = i["name"]
    Loan = i["loan_amount"]
    print(f"Name{name},Loan Amount {Loan}")

    Loan_details[name] = Loan
    print(Loan_details)