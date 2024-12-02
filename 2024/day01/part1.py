
file = open('2024/day01/input.txt')
lines = [l.strip().split('   ') for l in file.readlines()]

list1 = sorted([int(l[0]) for l in lines])
list2 = sorted([int(l[1]) for l in lines])

sum = sum([abs(list1[i] - list2[i]) for i in range(len(list1))])

print(sum)