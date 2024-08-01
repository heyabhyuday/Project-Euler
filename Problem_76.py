mod = (10 ** 9) + 7
UPPER = 1000

partitions = []
for i in range(UPPER + 1):
    partitions.append([None] * (UPPER + 1))
    for j in reversed(range(UPPER + 1)):
        if j == i:
            val = 1
        elif j > i:
            val = 0
        elif j == 0:
            val = partitions[i][j + 1]
        else:
            val = partitions[i][j + 1] + partitions[i - j][j]
        partitions[i][j] = val

t = int(input().strip())
for a0 in range(t):
    N = int(input().strip())
    print((partitions[N][1] - 1) % mod)

