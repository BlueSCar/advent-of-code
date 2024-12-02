file = open('day1/input.txt')
lines = [int(l.strip()) for l in file.readlines()]

previous = 9999999
count = 0

for line in lines:
    if line > previous:
        count += 1
        
    previous = line
    
print(count)