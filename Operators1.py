# Airthmatic operators

num1 = 10
num2 = 20

s1 = "R"
s2 = "T"

print(f"Addition of {num1} + {num2} = {num1 + num2}")
print(f"Addition of {s1} + {s2} = {s1 + s2}")

print(num1.__add__(num2))
print(s1.__add__(s2))

print(f"Addition of {num1} - {num2} = {num1 - num2}")
print(num1.__sub__(num2))

print(f"Multiplication of {num1} * {num2} = {num1 * num2}")
print(f"Multiplication of {s1} * {3} = {s1 * 3}")

print(num1.__mul__(num2))
print(s1.__mul__(3))

print(f"Division of {num1} / {num2} = {num1 / num2}")
print(f"floor Division of {num1} // {num2} = {num1 // num2}")

print(num1.__truediv__(num2))
print(num1.__floordiv__(num2))

print(f"modulus of {num1} % {num2} = {num1 % num2}")
print(f"exponatial of {num1} ** {num2} = {num1 ** num2}")

print(num1.__mod__(num2))

# Comparision Operators

num5 = 10 
num6 = 5

print(f"== operators {num5} == {num6} : {num5 == num6}")
print(num5.__eq__(num6))

print(f"!= operators {num5} != {num6} : {num5 != num6}")

print(f"> operators {num5} > {num6} : {num5 > num6}")

print(f"< operators {num5} < {num6} : {num5 < num6}")

print(f">= operators {num5} >= {num6} : {num5 >= num6}")

print(f"<= operators {num5} <= {num6} : {num5 <= num6}")

 # assignment operators

num7 = 10

num7 = num7 + num7
print(num7)
num7 += num7
print(num7)

num7 -= num7
print(num7)

num7 *= num7
print(num7)

num7 /= num7
print(num7)

num7 //= num7
print(num7)

num7 % num7
print(num7)

num7 **= num7
print(num7)

number1 = 20
number2 = 50

number1 &= number2
print(number1)

number1 |= number2
print(number1)

number1 ^= number2
print(number1)

number1 >>= number2
print(number1)

number1 <<= number2
print(number1)

# Logical Operator

num8 = 30
num9 = 50

print(num8 > 25 and num8 < 25)
print(num8 > 25 and num9 < 25)

print(num8 < 25 or num8 < 25)
print(num8 > 25 or num8 < 25)

print(not num8 > num9)
print(not num8 < num9)

# Bitwise operator

# Special operator
