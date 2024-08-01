# Problem 39: Integer Right Triangles
from math import gcd

UPPER = 5 * (10 ** 6)
plist = [0] * (UPPER + 1)
ans = [0] * (UPPER + 1)
ans[12] = 12

for a in range(1, 2001):
    for b in range(1, a):
        if (a + b) % 2 == 1 and gcd(a, b) == 1:
            p = 2 * a * a + 2 * a * b
            if p > UPPER:
                continue
            plist[p] += 1
            i = 2
            while i * p <= UPPER:
                plist[i * p] += 1
                i += 1

for i in range(13, UPPER):
    if plist[i] > plist[ans[i - 1]]:
        ans[i] = i
    else:
        ans[i] = ans[i - 1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(ans[n])
