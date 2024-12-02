from collections import Counter

file = open("day02/input.txt")
boxes = [l.strip() for l in file.readlines()]

most_common = ""

for i in range(len(boxes) - 1):
    box1 = boxes[i]
    
    for j in range(i + 1, len(boxes)):
        box2 = boxes[j]
        
        common = "".join([box1[k] for k in range(len(box1)) if box1[k] == box2[k]])
        if len(common) > len(most_common):
            most_common = common

print(most_common)