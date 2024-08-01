#Problem 46: Goldbach's Other Conjecture

UPPER_LIMIT = 10 ** 5
primes = set()
prime = [True] * (UPPER_LIMIT + 1)
doublesquares = [2 * i * i for i in range(1000)]

for i in range(3, int(UPPER_LIMIT ** 0.5) + 1, 2):
    if prime[i]:
        for j in range(i * 2, UPPER_LIMIT, i):
            prime[j] = False
    i += 1

for p in range(2, UPPER_LIMIT + 1):
    if prime[p]:
        primes.add(p)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    GBnum = 0

    for s in doublesquares:
        if s > n:
            break
        if (n - s) in primes:
            GBnum += 1

    print(GBnum)
