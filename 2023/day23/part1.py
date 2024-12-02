from collections import deque

DIRECTIONS = {
    ">": (0,1),
    "<": (0,-1),
    "^": (-1,0),
    "v": (1,0)
}

file = open("day23/input.txt")
lines = [l.strip() for l in file.readlines()]

rows = len(lines)
cols = len(lines[0])

start = (0, lines[0].index("."))
end = (len(lines) - 1, lines[-1].index("."))

q = deque([(start[0], start[1], set([start]))])
distances = []
while q:
    x, y, visited = q.popleft()
    
    symbol = lines[x][y]
    for d in DIRECTIONS:
        if symbol == d or symbol == ".":
            nx = x + DIRECTIONS[d][0]
            ny = y + DIRECTIONS[d][1]
            if nx == end[0] and ny == end[0]:
                distances.append(len(visited) - 1)
            elif nx >= 0 and ny >= 0 and nx < rows and ny < cols and (nx, ny) not in visited and lines[nx][ny] != "#":
                nv = visited.copy()
                nv.add((nx, ny))
                q.append((nx, ny, nv))
                
print(max(distances))