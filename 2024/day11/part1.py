file = open('2024/day11/input.txt', 'r')
stones = list(map(int, file.read().split(' ')))

blinks = 25
for i in range(blinks):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_stones.append(int(stone_str[:len(stone_str) // 2]))
            new_stones.append(int(stone_str[len(stone_str) // 2:]))
        else:
            new_stones.append(stone * 2024)
            
    stones = new_stones
    
print(len(stones))