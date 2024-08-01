#!/bin/python3

#Problem 2: Even Fibonacci Numbers

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prev = int(0)
    curr = int(1)
    sum = int(0)
    for a2 in range(n):
        next = prev + curr
        prev = curr
        curr = next
        if curr > n:
            print(sum)
            break
        if curr % 2 == 0:
            sum += curr


