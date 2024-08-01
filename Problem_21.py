#Problem 21: Amicable Sums

import sys

UPPER = 10 ** 5
dsums = [1] * (UPPER + 1)
asums = [0] * (UPPER + 1)

for i in range(2, UPPER):
    for j in range(2 * i, UPPER, i):
        dsums[j] += i

def isamicable(num): return num == dsums[dsums[num]]

for i in range(1, UPPER + 1):
    asums[i] = asums[i-1]
    if dsums[i] <= UPPER and dsums[i] != i and isamicable(i):
        asums[i] += i

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(asums[n])
