#!/bin/python3

#Problem 1: Multiples of 3 and 5

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    a = int(n/3)
    b = int(n/5)
    c = int(n/15)
    s = int(3*(a*(a+1)) + 5*(b*(b+1)) - 15*(c*(c+1))>>1)
    print(int(s))

