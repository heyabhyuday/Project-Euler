# Problem 82: Path Sum: Three Ways

N = int(input())

grid = []
for a0 in range(N):
    grid.append([int(x) for x in input().split()])

height = len(grid)
width = len(grid[0])
inf = 2 ** 32


def evaluate(x, y):
    if x < 0:
        return 0
    elif y < 0 or y >= height or x >= width:
        return inf
    else:
        return distance[y][x]


distance = [[0] * width for i in range(height)]


for x in range(width):
    for y in range(height):
        distance[y][x] = grid[y][x] + min(evaluate(x - 1, y), evaluate(x, y - 1))
    for y in reversed(range(height)):
        distance[y][x] = min(grid[y][x] + evaluate(x, y + 1), distance[y][x])


print(min(distance[y][-1] for y in range(height)))
print(inf)
