file = open('2024/day11/input.txt', 'r')
stones = list(map(int, file.read().split(' ')))

stone_dict = {}

def get_stone_result(stone, iterations_left):
    if iterations_left == 0:
        return 1
    
    if (stone, iterations_left) in stone_dict:
        return stone_dict[(stone, iterations_left)]
    
    if stone == 0:
        result = get_stone_result(1, iterations_left - 1)
        stone_dict[(stone, iterations_left)] = result
        return result
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        result = get_stone_result(int(stone_str[:len(stone_str) // 2]), iterations_left - 1) + get_stone_result(int(stone_str[len(stone_str) // 2:]), iterations_left - 1)
        stone_dict[(stone, iterations_left)] = result
        return result
    else:
        result = get_stone_result(stone * 2024, iterations_left - 1)
        return result
    
blinks = 75
total_stones = 0
for stone in stones:
    total_stones += get_stone_result(stone, blinks)
    
print(total_stones)