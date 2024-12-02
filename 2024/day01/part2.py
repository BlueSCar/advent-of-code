
file = open('2024/day01/input.txt')
lines = [l.strip().split('   ') for l in file.readlines()]

list1 = [int(l[0]) for l in lines]
list2 = [int(l[1]) for l in lines]

score = sum([i*len([j for j in list2 if j == i]) for i in list1])

print(score)