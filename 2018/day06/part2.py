import numpy as np

file = open("day06/input.txt")
coords = [tuple(map(int, [c] + l.strip().split(", "))) for c, l in enumerate(file.readlines(), 1)]

max_x = max([c[1] for c in coords]) + 1
max_y = max([c[2] for c in coords]) + 1

grid = list(np.full((max_x + 1, max_y + 1), -1))
region_size = 0

for i in range(max_x + 1):
    for j in range(max_y + 1):
        distances = sum([abs(c[1] - i) + abs(c[2] - j) for c in coords])
        grid[i][j] = distances
        
        if distances < 10000:
            region_size += 1

print(region_size)