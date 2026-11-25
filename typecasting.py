            # #  intger(decimal) convert (float, string , complex, boolean)

num1 = 10  # Num1 is :  10  type of num1 :  <class 'int'>
print("Num1 is : " ,num1, " type of num1 : " , type(num1))

float1 = float(num1) # flaot1 is :  10.0  type of flaot1 :  <class 'float'>
print("flaot1 is : " ,float1, " type of flaot1 : " , type(float1))

str1 = str(num1) # str1 is :  10  type of str1 :  <class 'str'>
print("str1 is : " ,str1, " type of str1 : " , type(str1))

com1 = complex(num1) # com1 is :  (10+0j)  type of com1 :  <class 'complex'>
print("com1 is : " ,com1, " type of com1 : " , type(com1))

bool1 = bool(num1) # bool1 is :  True  type of bool1 :  <class 'bool'>
print("bool1 is : " ,bool1, " type of bool1 : " , type(bool1))


            # #  Float convert (intger(decimal), string , complex, boolean)

num2 = 10.20  # Num2 is :  10.2  type of num2 :  <class 'float'>
print("Num2 is : " ,num2, " type of num2 : " , type(num2))

int1 = int(num2)  # int1 is :  10  type of int1 :  <class 'int'>
print("int1 is : " ,int1, " type of int1 : " , type(int1))

str2 = str(num2) # str2 is :  10.2  type of str2 :  <class 'str'>
print("str2 is : " ,str2, " type of str2 : " , type(str2))

com2 = complex(num2) # com2 is :  (10.2+0j)  type of com2 :  <class 'complex'> 
print("com2 is : " ,com2, " type of com2 : " , type(com2))

bool2 = bool(num2) # bool2 is :  True  type of bool2 :  <class 'bool'>
print("bool2 is : " ,bool2, " type of bool2 : " , type(bool2))


            #  String convert (intger(decimal), float , complex, boolean)

num3 = "10.20"   # num3 is :  10.20  type of num3 :  <class 'str'>
print("num3 is : " ,num3, " type of num3 : " , type(num3))

num4 = "10" # num4 is :  10  type of num4 :  <class 'str'>
print("num4 is : " ,num4, " type of num4 : " , type(num4))

name = "Ritik" # name is :  Ritik  type of name :  <class 'str'>
print("name is : " ,name, " type of name : " , type(name))


int2 = int(num3)  # ValueError: invalid literal for int() with base 10: '10.20' 
print("int2 is : " ,int2, " type of int2 : " , type(int2))

int3 = int(num4)  # int3 is :  10  type of int3 :  <class 'int'>
print("int3 is : " ,int3, " type of int3 : " , type(int3))

int4 = int(name)   # ValueError: invalid literal for int() with base 10: 'Ritik'
print("int4 is : " ,int4, " type of int4 : " , type(int4))


float2 = float(num3) # float2 is :  10.2  type of float2 :  <class 'float'>
print("float2 is : " ,float2, " type of float2 : " , type(float2))

float3 = float(num4)  # float3 is :  10.0  type of float3 :  <class 'float'>
print("float3 is : " ,float3, " type of float3 : " , type(float3))

float4 = float(name) # ValueError: could not convert string to float: 'Ritik'
print("float4 is : " ,float4, " type of float4 : " , type(float4))


com3 = complex(num3) # com3 is :  (10.2+0j)  type of com3 :  <class 'complex'>
print("com3 is : " ,com3, " type of com3 : " , type(com3))

com4 = complex(num4) # com4 is :  (10+0j)  type of com4 :  <class 'complex'>
print("com4 is : " ,com4, " type of com4 : " , type(com4))

com5 = complex(name) # ValueError: complex() arg is a malformed string
print("com5 is : " ,com5, " type of com5 : " , type(com5))


bool3 = bool(num3)  # bool3 is :  True  type of bool3 :  <class 'bool'>
print("bool3 is : " ,bool3, " type of bool3 : " , type(bool3))

bool4 = bool(num4)  # bool4 is :  True  type of bool4 :  <class 'bool'>
print("bool4 is : " ,bool4, " type of bool4 : " , type(bool4))

bool5 = bool(name)  # bool5 is :  True  type of bool5 :  <class 'bool'>
print("bool5 is : " ,bool5, " type of bool5 : " , type(bool5))


            # #  complex convert (intger(decimal), string , float, boolean)

num5 = 10 + 20j  # num5 (10+20j)  type of num5 :  <class 'complex'>
print("num5" ,num5, " type of num5 : " , type(num5))

int5 = int(num5)  # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
print("int5 is : " ,int5, " type of int5 : " , type(int5))

str3 = str(num5) # str3 is :  (10+20j)  type of str3 :  <class 'str'>
print("str3 is : " ,str3, " type of str3 : " , type(str3))

float5 = float(num5)  # TypeError: float() argument must be a string or a real number, not 'complex'
print("float5 is : " ,float5, " type of float5 : " , type(float5))

bool5 = bool(num5)  # bool5 is :  True  type of bool5 :  <class 'bool'>
print("bool5 is : " ,bool5, " type of bool5 : " , type(bool5))

