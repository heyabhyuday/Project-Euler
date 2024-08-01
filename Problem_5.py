#Problem 5: Smallest Multiple

import sys
import math


def arrayLCM(a):
    lcm = a[0]
    for i in range(1,len(a)):
        lcm = lcm * a[i]//math.gcd(lcm, a[i])
    return lcm


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lst = []
    for i in range(1, n+1):
        lst.append(i)
    print(arrayLCM(lst))
