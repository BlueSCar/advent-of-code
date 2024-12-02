from collections import Counter

file = open("day02/input.txt")
boxes = [l.strip() for l in file.readlines()]

dupes = 0
trips = 0

for box in boxes:
    c = Counter(box).values()
    
    if 2 in c:
        dupes += 1
        
    if 3 in c:
        trips += 1

print(dupes*trips)