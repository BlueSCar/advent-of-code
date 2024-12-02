file = open("day01/input.txt")
steps = [int(l.strip()) for l in file.readlines()]

frequencies = set([0])
current = 0
i = 0

while True:
    j = i % len(steps)
    step = steps[j]
    current += step
    
    if current in frequencies:
        break
    
    frequencies.add(current)
    i += 1

print(current)