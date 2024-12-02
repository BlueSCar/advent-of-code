from collections import defaultdict, deque

DIRECTIONS = [
    (0,1),
    (0,-1),
    (-1,0),
    (1,0)
]

file = open("day23/input.txt")
lines = [l.strip() for l in file.readlines()]

rows = len(lines)
cols = len(lines[0])

NODES = defaultdict(set)
for x in range(rows):
    for y in range(cols):
        if lines[x][y] != "#":
            for d in DIRECTIONS:
                nx = x + d[0]
                ny = y + d[1]
                if nx >= 0 and ny >= 0 and nx < rows and ny < cols and lines[nx][ny] != "#":
                    NODES[(x,y)].add((nx, ny, 1))
                    NODES[(nx,ny)].add((x,y,1))

keys = list(NODES.keys())
for n in keys:
    neighbors = NODES[n]
    if len(neighbors) == 2:
        n1 = neighbors.pop()
        n2 = neighbors. pop()
        NODES[n1[:-1]].remove((n[0], n[1], n1[2]))
        NODES[n1[:-1]].add((n2[0], n2[1], n1[2] + n2[2]))
        NODES[n2[:-1]].remove((n[0], n[1], n2[2]))
        NODES[n2[:-1]].add((n1[0], n1[1], n1[2] + n2[2]))
        
        NODES.pop(n)

start = (0, lines[0].index("."))
end = (len(lines) - 1, lines[-1].index("."))

q = deque([(start[0], start[1], 0)])
distances = []
visited = set()
while q:
    x, y, d = q.pop()
    if d == -1:
        visited.remove((x,y))
    elif (x,y) == end:
        distances.append(d)
    elif (x,y) not in visited:
        visited.add((x,y))
        q.append((x, y, -1))
        for n in NODES[(x,y)]:
            nd = d + n[-1]
            q.append((n[0], n[1], nd))
                
print(max(distances))