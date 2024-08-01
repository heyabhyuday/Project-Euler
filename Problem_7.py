#Problem 7: 10001st Prime
import sys

primes = []
UPPER_LIMIT = 1000000

prime = [True for i in range(UPPER_LIMIT + 1)]
p = 2
while p * p <= UPPER_LIMIT:
    if prime[p]:
        for i in range(p * p, UPPER_LIMIT + 1, p):
            prime[i] = False
    p += 1
for p in range(2, UPPER_LIMIT + 1):
    if prime[p]:
        primes.append(p)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primes[n-1])
