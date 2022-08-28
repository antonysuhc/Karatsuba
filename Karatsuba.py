#Need to operate in binary to make this actually faster than regular multiplication.

import math

def Karatsuba(a, b):
    if(a<=10 or b<= 10):
        return a*b
    else:
        bigNum = max(a, b)
        m = 10 ** (math.floor(math.log(bigNum, 10)/2))
        a1 = int(a/m)
        a2 = a % m
        b1 = int(b/m)
        b2 = b % m

        a1b1 = Karatsuba(a1, b1)
        a2b2 = Karatsuba(a2, b2)

        return (a1b1*m**2 + ((a1+a2)*(b1+b2)-a1b1-a2b2)*m + a2b2)

print(Karatsuba(177, 1823))
