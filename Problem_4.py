#Problem 4: Largest Palindrome Product

#!/bin/python3

import sys

plist = []
def palCheck(s): return str(s) == str(s)[::-1]
def giveLargest(x: int) -> int: return next(p for p in plist[::-1] if p < x)

for i in range(101100, 999999):
    if palCheck(i):
        if any(i % j == 0 for j in range(i//1000 + 1, 1000)):
            plist.append(i)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(giveLargest(n))

