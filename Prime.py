
num = int(input("Enter the number :"))
flag = 0
count = 0

if num < 2:
    print("Not prime")
    flag = 1
else:
    for i in range(2,num):
        if num % i == 0:
            print("Not prime")
            flag = 1
            break
if flag == 0:
    print("prime")


s = int(input("Enter the Starting point :"))
e = int(input("Enter the ending point :"))

for i in range(s,e+1):
    if i < 2:
        continue
    flag = 0
else:
    for j in range(2,i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        count = count + 1
        print(i)

print("count of prime number in given range :",count)

