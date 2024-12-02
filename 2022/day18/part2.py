import numpy as np
from collections import deque

file = open("day18/input.txt")
coords = [tuple(map(int, l.strip().split(","))) for l in file.readlines()]

DIRECTIONS = np.array([
    np.array((1, 0, 0)),
    np.array((-1, 0, 0)),
    np.array((0, -1, 0)),
    np.array((0, 1, 0)),
    np.array((0, 0, -1)),
    np.array((0, 0, 1))
])

min_x = min([c[0] for c in coords]) - 1
min_y = min([c[1] for c in coords]) - 1
min_z = min([c[2] for c in coords]) - 1

max_x = max([c[0] for c in coords]) + 1
max_y = max([c[1] for c in coords]) + 1
max_z = max([c[2] for c in coords]) + 1

start = (min_x, min_y, min_z)
visited = set()
q = deque([start])

while q:
    current = q.pop()
    for d in DIRECTIONS:
        next = tuple(np.array(current) + d)
        if next not in visited and next not in coords and next[0] >= min_x and next[0] <= max_x and next[1] >= min_y and next[1] <= max_y and next[2] >= min_z and next[2] <= max_z:
            visited.add(next)
            q.append(next)

sides = 0
for c in coords:
    for d in DIRECTIONS:
        adj = tuple(np.array(c) + d)
        if adj not in coords and adj in visited:
            sides += 1

print(sides)