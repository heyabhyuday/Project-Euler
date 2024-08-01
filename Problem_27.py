#Problem 27: Quadratic Primes
import sys

def isPrime(n):
  if n in [2, 3, 5, 7]: return True
  if n < 2 or n % 2 == 0: return False
  if n % 3 == 0: return False
  r = int(n ** 0.5)
  f = 5
  while(f <= r):
    if n % f == 0: return False
    if n % (f + 2) == 0: return False
    f += 6
  return True

n= int(input().strip())
co1, co2, count = 0, 0, 0
for b in range(1,n):
    for a in range(-n,0,1):
        len_count = 0
        while isPrime(int(len_count ** 2) + a * len_count + b):
            len_count += 1
        if len_count > count:
            co1, co2 = a, b
            count = len_count

print(co1, co2)
