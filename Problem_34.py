#Problem 34: Digit Factorials
import sys

def fact(num):
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f

n = int(input().strip())

ans = 0
for i in range(19, n):
    s = sum(fact(int(c)) for c in str(i))
    if s % i == 0:
        ans += i

print(ans)
