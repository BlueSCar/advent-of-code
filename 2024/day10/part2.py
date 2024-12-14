file = open('2024/day10/input.txt', 'r')
map = [list(map(int, l)) for l in file.read().split('\n')]

trailheads = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            trailheads.append((i, j))
   
def get_trails(i, j, visited, rating):
    if (i, j) in visited:
        return 0
    
    if map[i][j] == 9:
        return 1
           
    if i > 0 and map[i-1][j] - map[i][j] == 1:
        rating += get_trails(i-1, j, visited.copy(), 0)
        
    if i < len(map) - 1 and map[i+1][j] - map[i][j] == 1:
        rating += get_trails(i+1, j, visited.copy(), 0)
        
    if j > 0 and map[i][j-1] - map[i][j] == 1:
        rating += get_trails(i, j-1, visited.copy(), 0)
        
    if j < len(map[i]) - 1 and map[i][j+1] - map[i][j] == 1:
        rating += get_trails(i, j+1, visited.copy(), 0)
        
    return rating 
             
ratings = 0
for trailhead in trailheads:
    visited = set()
    
    rating = get_trails(trailhead[0], trailhead[1], visited.copy(), 0)
    ratings += rating
    

print(ratings)