#!/bin/python3

#Problem 3: Largest Prime Factor

import sys
import math

def largest(n):
    while True:
        f = factor(n)
        if f < n:
            n //= f
        else:
            return n


def factor(n):
    assert n >= 2
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return i
    return n

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest(n))
