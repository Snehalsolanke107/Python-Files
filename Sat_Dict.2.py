sub_marks = {}
print(type(sub_marks))

sub_marks['Python'] = 55
sub_marks['MySQL'] = 75
sub_marks['PowerBI'] = 85

print(sub_marks)

print(sub_marks["MySQL"])
print(sub_marks["Python"])
print(sub_marks["PowerBI"])

sub_marks["MySQL"] = sub_marks["MySQL"]+5
print(sub_marks)

del sub_marks["PowerBI"]
print(sub_marks)

emp_details = {
    101 : {"Name" : "Snehal Solanke","Dept" : "Data Analyst","salary" : 69000},
    102 : {"Name" : "Ritika Naik","Dept" : "Data Science","salary" : 80000}
}

print(emp_details[101]["salary"])
emp_details[101]["city"] = "Pune"
print(emp_details)

print(emp_details[102]["salary"])
emp_details[102]["city"] = "Mumbai"
print(emp_details)

for i in emp_details.values():
    print(i)

for i in emp_details.items():
    print(i)

for i,j in emp_details.items():
    print(i)