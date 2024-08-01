#Problem 20: Factorial digit sum

import sys

def fdsum(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return sum(int(c) for c in str(f))

silo = []
for i in range(1000):
    silo.append(fdsum(i))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(silo[n])
