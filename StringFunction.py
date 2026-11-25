s1 = "pratik"

print(f"s1 : {s1} ")

print(f"use upper method : {s1.upper()}")  #  PRATIK

print(f"use isupper method : {s1.isupper()}")


s2 = "ROHIT"

print(f"s2 : {s2} ")

print(f"use lower method : {s2.lower()}")  # rohit 

print(f"use islower method : {s2.islower()}")

s3 = "Python Programming Language"

print(f"s3 : {s3}")
print(f"use captilize method : {s3.capitalize()}")  #  Python programming language

print(f"use title method : {s3.title()}")  # Python Programming Language


print(f"use istitle method : {s3.istitle()}")


s4 = "     python"

print(f"s4 : {s4}")
print(f"use strip method : {s4.strip()}")
print(f"use strip method : {s3.strip()}") # Python Programming Language

s5 = "python is genral purpose language"

print(f"s5 : {s5}")

split = s5.split() # ['python', 'is', 'genral', 'purpose', 'language']
print(f"use split method : {split}") 

join = "-".join(split)  #  python is genral purpose language
print(f"use join method : {join}") 

partition =  s5.partition("h") #  ('pyt', 'h', 'on is genral purpose language')
print(f"use partition method : {partition}") 

join1 = " ".join(partition)  #  pyt h on is genral purpose language
print(f"use join method : {join1}")  

rpartition =  s5.rpartition("g") #  ('python is genral purpose langua', 'g', 'e')
print(f"use rpartition method : {rpartition}") 


num1 = 91
print(f"use chr function : {chr(num1)}")

chr = "["
print(f"Use ord Function : {ord(chr)}")

s6 = "python support OOPs"

print(f"use Find Method : {s6.find("s")}")  # 7 
print(f"use index Method : {s6.index("z")}")  #  7