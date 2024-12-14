file = open('2024/day09/input.txt', 'r')
contents = file.read()

free_blocks = []
used_blocks = []
current_id = 0
current_position = 0
is_free = False

for i in range(len(contents)):
    block_length = int(contents[i])
    if not is_free:
        used_blocks.append([current_position, block_length, current_id])
        current_id += 1
        current_position += block_length
    else:
        free_blocks.append([current_position, block_length])
        current_position += block_length
        
    is_free = not is_free

for used in used_blocks[::-1]:
    for free in free_blocks:
        if used[0] > free[0] and used[1] <= free[1]:
            used[0] = free[0]
            free[1] -= used[1]
            free[0] += used[1]
            
checksum = 0
for used in used_blocks:
    checksum += (used[2] * sum(range(used[0], used[0] + used[1])))
            
print(checksum)