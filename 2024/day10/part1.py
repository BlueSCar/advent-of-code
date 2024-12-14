file = open('2024/day10/input.txt', 'r')
map = [list(map(int, l)) for l in file.read().split('\n')]

trailheads = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            trailheads.append((i, j))
   
def get_peaks(i, j, visited, peaks):
    if (i, j) in visited:
        return
    
    if map[i][j] == 9:
        peaks.add((i, j))
        visited.add((i, j))
        return
           
    if i > 0 and map[i-1][j] - map[i][j] == 1:
        get_peaks(i-1, j, visited, peaks)
        
    if i < len(map) - 1 and map[i+1][j] - map[i][j] == 1:
        get_peaks(i+1, j, visited, peaks)
        
    if j > 0 and map[i][j-1] - map[i][j] == 1:
        get_peaks(i, j-1, visited, peaks)
        
    if j < len(map[i]) - 1 and map[i][j+1] - map[i][j] == 1:
        get_peaks(i, j+1, visited, peaks)    
             
score = 0
for trailhead in trailheads:
    visited = set()
    peaks = set()
    
    get_peaks(trailhead[0], trailhead[1], visited, peaks)
    score += len(peaks)
    

print(score)