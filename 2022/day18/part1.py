import numpy as np

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

sides = 0
for c in coords:
    for d in DIRECTIONS:
        adj = np.array(c) + d
        if tuple(adj) not in coords:
            sides += 1

print(sides)