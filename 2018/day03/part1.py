import numpy as np
import re

CLAIM_PATTERN = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

file = open("day03/input.txt")
claims = [tuple(map(int, CLAIM_PATTERN.match(l.strip()).groups())) for l in file.readlines()]

max_x = max([c[1] + c[3] for c in claims])
max_y = max([c[2] + c[4] for c in claims])

states = list(np.full((max_x, max_y), 0))

for (claim_no, x, y, width, height) in claims:
    for i in range(x, x + width):
        for j in range(y, y + height):
            states[i][j] += 1

activated = len([y for x in states for y in x if y > 1])

print(activated)