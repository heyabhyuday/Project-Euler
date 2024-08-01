#Problem 10: Summation of Primes

import sys

UPPER_LIMIT = 10 ** 6
prime = [True] * (UPPER_LIMIT + 1)
sums = []

for i in range(3, int(UPPER_LIMIT ** 0.5) + 1, 2):
    if prime[i]:
        for j in range(i ** 2, UPPER_LIMIT, i):
            prime[j] = False
primes = [2] + [i for i in range(3, UPPER_LIMIT, 2) if prime[i]]

tempsum, c = 0, 0
for i in range(UPPER_LIMIT):
    if primes[c] <= i:
        tempsum += primes[c]
        if c + 1 < len(primes):
            c += 1
    sums.append(tempsum)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sums[n])
