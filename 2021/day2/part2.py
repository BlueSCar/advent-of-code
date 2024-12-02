file = open('day2/input.txt')
inputs = [l.strip().split(' ') for l in file.readlines()]

aim = 0
horizontal = 0
depth = 0

for i in inputs:
    action = i[0]
    units = int(i[1])
    
    if action == 'forward':
        horizontal += units
        depth += aim*units
    elif action == 'up':
        aim -= units
    elif action == 'down':
        aim += units
        
print(horizontal*depth)