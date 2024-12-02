file = open("day22/input.txt")
coords = sorted([tuple([tuple(map(int, c.split(","))) for c in l.strip().split("~")]) for l in file.readlines()], key=lambda x: x[0][2])
bricks = dict([(i, (v[0], v[1], set())) for (i, v) in enumerate(coords)])

# for brick in bricks:
#     if brick[0][0] > brick[1][0] or brick[0][1] > brick[1][1] or brick [0][2] > brick[1][2]:
#         print("stuff is not ordered mang")
#         break

heights = {}
for i in bricks:
    brick = bricks[i]
    max_z = 0
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if (x,y) in heights and heights[(x,y)][0] > max_z:
                max_z = heights[(x,y)][0]
                
    new_z = max_z + 1
    z_diff = brick[1][2] - brick[0][2]
    bricks[i] = ((brick[0][0], brick[0][1], new_z), (brick[1][0], brick[1][1], new_z + z_diff), bricks[i][2])
    for x in range(brick[0][0], brick[1][0] + 1):
        for y in range(brick[0][1], brick[1][1] + 1):
            if (x,y) not in heights:
                heights[(x,y)] = (new_z + z_diff, i)
            elif heights[(x,y)][0] < new_z:
                if new_z - heights[(x,y)][0] == 1:
                    bricks[i][2].add(heights[(x,y)][1])
                heights[(x,y)] = (new_z + z_diff, i)
                
needed = sorted(list(set([bricks[b][2].pop() for b in bricks if len(bricks[b][2]) == 1])))
safe = len(bricks) - len(needed)

print(safe)