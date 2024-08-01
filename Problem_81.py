#Problem 81: Path Sum - Two Ways

N = int(input())
grid = []
for a0 in range(N):
    grid.append([int(x) for x in input().split()])

L = len(grid)
for i in reversed(range(L)):
    for j in reversed(range(L)):
        if i + 1 < L and not j + 1 < L:
            temp = grid[i + 1][j]
        elif j + 1 < L and not i + 1 < L:
            temp = grid[i][j + 1]
        elif i + 1 < L and j + 1 < L:
            temp = min(grid[i + 1][j], grid[i][j + 1])
        else:
            temp = 0
        grid[i][j] += temp

print(grid[0][0])
