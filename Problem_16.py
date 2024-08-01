#Problem 16: Power Digit Sum
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    pds = 0
    ex = 2 ** n
    for c in str(ex):
        pds += int(c)
    print(pds)
