file = open('day3/input.txt')
lines = [l.strip() for l in file.readlines()]



counts = [sum(int(line[i]) for line in lines) for i in range(len(lines[0]))]

def get_o2(numbers):
    digit = '0'
    if sum([int(n[0]) for n in numbers]) >= (len(numbers) / 2):
        digit = '1'
    
    if len(numbers[0]) == 1:
        return digit
    else:
        return digit + get_o2([number[1:] for number in numbers if number[0] == digit])
    
def get_co2(numbers):
    if len(numbers) == 1:
        return numbers[0]
    
    digit = '0'
    if sum([int(n[0]) for n in numbers]) < (len(numbers) / 2):
        digit = '1'
    
    if len(numbers[0]) == 1:
        return digit
    else:
        return digit + get_co2([number[1:] for number in numbers if number[0] == digit])
    
oxygen_bin = get_o2(lines)
co2_bin = get_co2(lines)

oxygen = int(oxygen_bin, 2)
co2 = int(co2_bin, 2)

print(oxygen * co2)
