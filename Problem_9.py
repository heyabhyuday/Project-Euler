#Problem 9: Special Pythagorean Triplet

#!/bin/python3

import sys

def special(N):
    prod = -1
    for a in range(1, (N//3) + 1):
        b = N * (N - 2 * a)//(2 * (N - a))
        c = N - a - b
        if a ** 2 + b ** 2 == c ** 2:
            prod = max(prod, a * b * c)
    return prod

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(special(n))
