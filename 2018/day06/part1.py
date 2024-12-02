import numpy as np

file = open("day06/input.txt")
coords = [tuple(map(int, [c] + l.strip().split(", "))) for c, l in enumerate(file.readlines(), 1)]

max_x = max([c[1] for c in coords]) + 1
max_y = max([c[2] for c in coords]) + 1

grid = list(np.full((max_x + 1, max_y + 1), -1))
areas = {}

for i in range(max_x + 1):
    for j in range(max_y + 1):
        distances = sorted([(abs(c[1] - i) + abs(c[2] - j), c[0]) for c in coords])
        
        if distances[0][0] != distances[1][0]:
            grid[i][j] = distances[0][1]
            if distances[0][1] not in areas:
                areas[distances[0][1]] = 1
            else:
                areas[distances[0][1]] += 1
            
unbounded = set(list(grid[0]) + list(grid[max_x]) + list([grid[i][0] for i in range(max_x + 1)]) + list([grid[i][max_y] for i in range(max_x + 1)]))

highest = max([areas[i] for i in areas if i not in unbounded])

print(highest)