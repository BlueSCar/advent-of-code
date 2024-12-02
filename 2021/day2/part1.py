file = open('day2/input.txt')
inputs = [l.strip().split(' ') for l in file.readlines()]

horizontal = sum([int(i[1]) for i in inputs if i[0] == 'forward'])
depth = sum([int(i[1]) for i in inputs if i[0] == 'down']) - sum([int(i[1]) for i in inputs if i[0] == 'up'])

print(horizontal*depth)