#Problem 37: Truncatable Primes



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


UPPER_LIMIT = 10 ** 6
prime = ([False] * 2) + [True] * (UPPER_LIMIT - 1)
p = 2
while p * p <= UPPER_LIMIT:
    if prime[p]:
        for i in range(p * p, UPPER_LIMIT + 1, p):
            prime[i] = False
    p += 1

def isTruncatable(n):
    i = 10
    while i <= n:
        if not prime[n % i]:
            return False
        i *= 10

    while n > 0:
        if not prime[n]:
            return False
        n //= 10
    return True

n = int(input().strip())
truncsum = 0
for i in range(10, n):
    if isTruncatable(i):
        print(i)
        truncsum += i
print(truncsum)
# print(prime)
