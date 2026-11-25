s1 = "abc"
s2 = "1234"
s3 = "6.34"
s4 = "  "
s5 = "Roshan1234"

print(f"use isalpha method on (s1) : {s1.isalpha()}") # True

print(f"use isalpha method on (s2) : {s2.isalpha()}") # False

print(f"use isalpha method on (s3) : {s3.isalpha()}") # False

print(f"use isalpha method on (s4) : {s4.isalpha()}") # False

print(f"use isalpha method on (s5) : {s5.isalpha()}") # False


print(f"use isnumeric method on (s1) : {s1.isnumeric()}") # False

print(f"use isnumeric method on (s2) : {s2.isnumeric()}") # True

print(f"use isnumeric method on (s3) : {s3.isnumeric()}") # False

print(f"use isnumeric method on (s4) : {s4.isnumeric()}") # False

print(f"use isnumeric method on (s5) : {s5.isnumeric()}") # False


print(f"use isalnum method on (s1) : {s1.isalnum()}") # True

print(f"use isalnum method on (s2) : {s2.isalnum()}") # True

print(f"use isalnum method on (s3) : {s3.isalnum()}") # False

print(f"use isalnum method on (s4) : {s4.isalnum()}") # False

print(f"use isalnum method on (s5) : {s5.isalnum()}") # True


print(f"use isspace method on (s1) : {s1.isspace()}") # False

print(f"use isspace method on (s2) : {s2.isspace()}") # False

print(f"use isspace method on (s3) : {s3.isspace()}") # False

print(f"use isspace method on (s4) : {s4.isspace()}") # True

print(f"use isspace method on (s5) : {s5.isspace()}") # False



print(f"use isdigit method on (s2) : {s2.isdigit()}") # 

print(f"use isdigit method on (s3) : {s3.isdigit()}") # 

print(f"use isdecimal method on (s2) : {s2.isdecimal()}") # 

print(f"use isdecimal method on (s3) : {s3.isdecimal()}") # 

# WAP to check string is empty or not 

str1 ="abc"
if str1 == " ":
    print("yes")
else :
    print("no")


s6 = "\t"

print(f"use is isprintable method : {s6.isprintable()}")

from keyword import iskeyword
print("Hello".isidentifier())

print(iskeyword("Hello"))

print("Python programming".startswith("P"))

print("Python programming".endswith("g"))

print(sorted("AbabCDa" , reverse=True))

print(len("Rohit"))

print("48".zfill(1))

print("jjvbvjbkj".count("j"))

print("jjvbvjbkj".count("j",3))

print("jjvbvjbkj".count("j",4,7))


print("Python".replace("Python" , "MySQL"))

s8 = "abc"
s8[0] = "10"

del s8

print(s8)