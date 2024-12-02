file = open("day01/input.txt")
frequency = sum([int(l.strip()) for l in file.readlines()])

print(frequency)