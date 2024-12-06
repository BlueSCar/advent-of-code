file = open("2024/day04/input.txt")
lines = [line.strip() for line in file.readlines()]

xmas_count = 0

permutations = [
    ('M', 'M', 'S', 'S'),
    ('S', 'S', 'M', 'M'),
    ('M', 'S', 'M', 'S'),
    ('S', 'M', 'S', 'M')
]

def is_x_mas(box: list[str]):
    if box[1][1] != "A":
        return False
    elif (box[0][0], box[0][2], box[2][0], box[2][2]) not in permutations:
        return False
    
    return True

for i in range(2, len(lines)):
    for j in range(2, len(lines[0])):
        if is_x_mas([lines[i-2][j-2:j+1], lines[i-1][j-2:j+1], lines[i][j-2:j+1]]):
            xmas_count += 1
            
print(xmas_count)