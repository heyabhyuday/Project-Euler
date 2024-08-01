# Problem 41: Pandigital Primes
from itertools import permutations
from bisect import bisect_left

def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


pds = []
for i in range(4, 11):
    pdstr = ""
    for j in range(1, i):
        pdstr += str(j)
    pds.append(pdstr)


def genPanPrimes(pandigits):
    perms = permutations(pandigits)
    for perm in list(perms):
        temp = int("".join(perm))
        if isPrime(temp):
            panprimes.append(temp)


panprimes = []
i = 0
for pd in pds:
    i += 1
    genPanPrimes(pd)


# def getMaxPanPrime(n):
#     maxp = -1
#     for p in panprimes:
#         if p > n:
#             return maxp
#         maxp = p


# print(panprimes[-1], max(panprimes))
# print(isPrime(987456231))
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    idx = bisect_left(panprimes, n)
    if idx < len(panprimes) and panprimes[idx] <= n:
        print(panprimes[idx])
    elif panprimes[idx - 1] <= n:
        print(panprimes[idx - 1])
    else:
        print(-1)
