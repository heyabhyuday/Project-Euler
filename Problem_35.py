#Problem 35: Circular Primes
import sys

primes = [2, 3, 5]

def sieve(u):
    prime = [True for i in range(u + 1)]
    p = 2
    while p * p <= u:
        if prime[p]:
            for i in range(p * p, u + 1, p):
                prime[i] = False
        p += 1

    for p in range(6, u + 1):
        if prime[p]:
            q = str(p)
            if '0' in q or '2' in q or '4' in q or '5' in q or '6' in q or '8' in q:
                continue
            else:
                primes.append(p)

def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input().strip())
sieve(n)
csum = 0

for p in primes:
    flag = True
    q = str(p)
    strl = len(q)
    if strl == 1:
        csum += p
    else:
        for i in range(1, strl):
            q2 = q[strl-i:] + q[:strl-i]
            p2 = int(q2)
            if not isPrime(p2):
                flag = False
                break
        if flag:
            csum += p

print(csum)
