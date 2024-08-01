#Problem 32: Pandigital Products
import sys
import math

digits = {4:'1234',5:'12345',6:'123456',7:'1234567',8:'12345678',9:'123456789'}

def panProd(x, d):
    temp = 0
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            str1 = str(x) + str(i) + str(x//i)
            if "".join(sorted(str1)) == digits[d]:
                return True
    return False

n = int(input().strip())
print(sum(i for i in range(1, 10000) if panProd(i, n)))
