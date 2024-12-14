import numpy as np

file = open('2024/day09/input.txt', 'r')
contents = file.read()

blocks = []
current_id = 0
is_free = False

for i in range(len(contents)):
    if not is_free:
        blocks += np.repeat(current_id, int(contents[i])).tolist()
        current_id += 1
    else:
        blocks += np.repeat('.', int(contents[i])).tolist()
        
    is_free = not is_free


filler_index = 1
for i in range(len(blocks)):
    while blocks[-filler_index] == '.':
        filler_index += 1
    
    filler = blocks[-filler_index]
    if blocks[i] == '.':
        new_blocks = blocks[:i] + [filler] + blocks[i+1:-filler_index] + ['.']
        if filler_index > 1:
            new_blocks += blocks[-filler_index+1:]
        blocks = new_blocks
        
    if i >= len(blocks) - filler_index:
        break
    
checksum = 0
for i in range(len(blocks)):
    if blocks[i] == '.':
        break
    
    checksum += int(blocks[i]) * i

print(checksum)