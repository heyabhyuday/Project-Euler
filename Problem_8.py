#Problem 8: Largest Product in a Series
import sys

def maxprod(N, l):
    maxprod = 0
    for i in range(len(N) - k):
        prod = 1
        for j in range(i, i + k):
            prod *= int(N[j])
        if prod >= maxprod:
            maxprod = prod
    return maxprod

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(maxprod(str(num), k))
