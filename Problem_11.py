#Problem 11: Largest Product in a Grid

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

product = 0

# Max Horizontal Product
temp = [j[i - 3] * j[i - 2] * j[i - 1] * j[i] for j in grid for i in range(3, 20)]
product = max(temp) if max(temp) > product else product

# Max Vertical Product
temp = [grid[i - 3][j] * grid[i - 2][j] * grid[i - 1][j] * grid[i][j] for j in range(0, 20) for i in range(3, 20)]
product = max(temp) if max(temp) > product else product

# Max Right Oblique Product
temp = [grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3] for j in range(0, 17) for i in
        range(0, 17)]
product = max(temp) if max(temp) > product else product

# Max Left Oblique Product
temp = [grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3] for j in range(19, 2, -1) for i
        in range(0, 17)]
product = max(temp) if max(temp) > product else product

print(product)
