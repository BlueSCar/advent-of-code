file = open('2024/day08/input.txt')
grid = [list(l.strip()) for l in file.readlines()]

frequencies = dict()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != '.':
            if grid[i][j] not in frequencies:
                frequencies[grid[i][j]] = [(i, j)]
            else:
                frequencies[grid[i][j]].append((i, j))
                
antinodes = set()
grid_height = len(grid)
grid_width = len(grid[0])

for key in frequencies:
    antennas = frequencies[key]
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            height_diff = antennas[i][0] - antennas[j][0]
            width_diff = antennas[i][1] - antennas[j][1]
            
            point1 = (antennas[i][0] + height_diff, antennas[i][1] + width_diff)
            point2 = (antennas[j][0] - height_diff, antennas[j][1] - width_diff)
            
            if 0 <= point1[0] <= grid_height - 1 and 0 <= point1[1] <= grid_width - 1:
                antinodes.add(point1)
            
            if 0 <= point2[0] <= grid_height - 1 and 0 <= point2[1] <= grid_width - 1:
                antinodes.add(point2)

print(len(antinodes))