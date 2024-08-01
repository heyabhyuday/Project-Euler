#Problem 18: Maximum Path Sum I
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    t = []
    for a1 in range(n):
        t.append(list(map(int, input().split())))
    r = n-2
    while r >= 0:
        for i in range(len(t[r])):
            t[r][i] += max(t[r + 1][i], t[r + 1][i + 1])
        r -= 1
    print(t[0][0], len(t[r]))
