#Problem 25: N-digit Fibonacci Number
UPPER_LIMIT = 23923
fibs = [0, 1]
a, b = 1, 1
d = 10

for i in range(3, UPPER_LIMIT):
    a, b = b, a+b
    if b >= d:
        d *= 10
        fibs.append(i)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fibs[n])
