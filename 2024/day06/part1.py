import numpy as np

contents = open("2024/day06/input.txt")
grid = [list(line.strip()) for line in contents]

directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

obstacles = set()
current = None
direction = 0
visited = set()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            obstacles.add((i, j))
        if grid[i][j] == "^":
            current = (i, j)
            
while current[0] >= 0 and current[0] < len(grid) and current[1] >= 0 and current[1] < len(grid[0]):
    visited.add(current)
    next = tuple(np.add(current, directions[direction % 4]))
    while next in obstacles:
        direction += 1
        next = tuple(np.add(current, directions[direction % 4]))
    
    current = next

print(len(visited))