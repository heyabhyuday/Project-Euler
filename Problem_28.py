# Problem 28: Number Spiral Diagnosis
mod = (10 ** 9) + 7

# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     result = 1
#     result += sum(4 * i * i - 6*(i - 1) for i in range(3, n + 1, 2))
#     print(result % mod)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) // 2
    result = ((4 * n * (n + 1) * (2 * n + 1) // 6 + (n * (n + 1) // 2) + n + 1) * 4 - 4) + 1
    print(result % mod)

