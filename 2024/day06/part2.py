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
og_path = list()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            obstacles.add((i, j))
        if grid[i][j] == "^":
            current = (i, j)
            
while current[0] >= 0 and current[0] < len(grid) and current[1] >= 0 and current[1] < len(grid[0]):
    if current not in og_path:
        og_path.append(current)
    next = tuple(np.add(current, directions[direction % 4]))
    while next in obstacles:
        direction += 1
        next = tuple(np.add(current, directions[direction % 4]))
    
    current = next
    
loops = 0
obstacles = list(obstacles)
print(f"path length: {len(og_path)}")
for i in range(1, len(og_path)):
    if i % 100 == 0:
        print(f"i: {i}")
    
    blockers = obstacles.copy() + [og_path[i]]
    current = og_path[0] + (0,)
    direction = 0
    visited = set()
    
    while current[0] >= 0 and current[0] < len(grid) and current[1] >= 0 and current[1] < len(grid[0]):
        if current in visited:
            loops += 1
            break
        visited.add(current)
        next = tuple(np.add((current[0], current[1]), directions[direction % 4]))
        while next in blockers:
            direction += 1
            next = tuple(np.add((current[0], current[1]), directions[direction % 4]))
            
        current = next + (direction % 4,)

print(loops)