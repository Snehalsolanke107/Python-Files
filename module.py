# modules 
    #  collection of method function , class , variable 
    #  modules mean single .py file 

# package 
    # collection of modules means multiple .py file 
    # identify using __init__.py file. this file will be empty 

# Types of modules 
    # 1. user define
    # 2. pre-define/ bulit-in (csv , os , functool, keyword , pathlib, abc, math , etc )
    # 3. third party (pandas , numpy , matplotlib, django , pymysql , mysql-connector )

# pre-define 

import math 

# print(math.ceil(10.5))
# print(math.floor(10.2))
# print(math.factorial(20))

import random as r
import string as s

# print(r.randint(0,9),r.choice(s.ascii_letters),r.choice(s.ascii_letters), r.randint(0,9), r.choice(s.ascii_letters),r.randint(0,9), r.randint(0,9))

from collections import deque

# d1 = deque([10,20,30])

# d1.rotate(4)
# print(d1)

# d2 = {}
# print(d2['name'])

from collections import *

# d3 = defaultdict(int)

# d3["name"]

# print(d3)

str1 = "qwertyuioasdfghjkzxcvbnmqwertyuisdfghcv"
# o/p  d4 = {"a":count,........,"z":count}
d = {}
for i in str1:
    d[i] = str1.count(i)

# print(d)

# print(Counter(str1))
