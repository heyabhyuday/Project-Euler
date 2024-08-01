#Problem 12: Highly Divisible Triangular Number
import sys

def genDivs(x):
    divs = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if x // i == i:
                divs += 1
            else:
                divs += 2
    return divs

def getDivs(n):
    for i in range(1, 50000):
        if i % 2 == 0:
            c = genDivs(i//2) * genDivs(i+1)
        else:
            c = genDivs(i) * genDivs((i+1)/2)

        if c > n:
            return (i * (i+1))//2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(getDivs(n))
