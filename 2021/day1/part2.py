file = open('day1/input.txt')
lines = [int(l.strip()) for l in file.readlines()]

sums = [lines[i] + lines[i+1] + lines[i+2] for i in range(0, len(lines) - 2)]
increases = [sums[i] for i in range(1, len(sums)) if sums[i] > sums[i-1]]

print(len(increases))