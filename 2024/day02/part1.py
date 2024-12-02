file = open('2024/day02/input.txt')
lines = [[int(i) for i in l.strip().split(' ')] for l in file.readlines()]

safe = 0

for line in lines:
    direction = 0
    is_safe = True
    for i in range(1, len(line)):
        diff = line[i] - line[i - 1]
        if direction == 0:
            direction = diff
            
        if (direction < 0 and diff > 0) or (direction > 0 and diff < 0) or abs(diff) > 3 or abs(diff) == 0:
            is_safe = False
            break
    
    if is_safe:
        safe += 1

print(safe)