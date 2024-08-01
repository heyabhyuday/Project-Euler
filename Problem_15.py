#Problem 15: Lattice Paths

import sys
mod = (10 ** 9) + 7

def fact(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f

def paths(a, b): return fact(a + b) // (fact(a) * fact(b)) % mod

t = int(input().strip())
for a0 in range(t):
    n, m = input().split()
    n = int(n)
    m = int(m)
    print(paths(n, m))
