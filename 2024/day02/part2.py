file = open('2024/day02/input.txt')
lines = [[int(i) for i in l.strip().split(' ')] for l in file.readlines()]

def is_report_safe(line, recurse=True):
    direction = 0
    for i in range(1, len(line)):
        diff = line[i] - line[i - 1]
        if direction == 0:
            direction = diff
            
        if (direction < 0 and diff > 0) or (direction > 0 and diff < 0) or abs(diff) > 3 or abs(diff) == 0:
            if recurse:
                return is_report_safe(line[:i] + line[i + 1:], False)
            else:
                return False
    
    return True


safe = 0
for line in lines:
    is_safe = is_report_safe(line) or is_report_safe(line[1:], False) or is_report_safe(line[:1] + line[2:], False)
    
    if is_safe:
        safe += 1

print(safe)