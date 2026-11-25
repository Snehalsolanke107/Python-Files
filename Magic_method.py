# Fraction calculater

class Fraction:
    def __init__(self,num,den):
        # set a values for num, deno
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_deno = self.den * other.den

        return Fraction(new_num,new_deno)

    def __sub__(self, other):
            new_num = self.num * other.den - self.den * other.num
            new_deno = self.den * other.den
    
            return Fraction(new_num,new_deno)
    def __mul__(self, other):
                new_num = self.num * other.num
                new_deno = self.den * other.den
        
                return Fraction(new_num,new_deno)
    def __truediv__(self, other):
                new_num = self.num * other.den 
                new_deno = self.den * other.num
        
                return Fraction(new_num,new_deno)
    
f1 = Fraction(3,5)
print(f1)
f2 = Fraction(3,4)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)

