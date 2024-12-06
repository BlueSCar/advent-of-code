import numpy as np

file = open("2024/day04/input.txt")
lines = [line.strip() for line in file.readlines()]

xmas_count = 0

for line in lines:
    xmas_count += line.count("XMAS")
    xmas_count += line.count("SAMX")
    
for i in range(len(lines)):
    vert = "".join([l[i] for l in lines])
    xmas_count += vert.count("XMAS")
    xmas_count += vert.count("SAMX")
    
np_array = np.array([[l for l in line] for line in lines])
diagonals = [np_array[::-1,:].diagonal(i) for i in range(-np_array.shape[0]+1,np_array.shape[1])]
diagonals.extend(np_array.diagonal(i) for i in range(np_array.shape[1]-1,-np_array.shape[0],-1))
diagonal_lines = ["".join([l for l in line]) for line in diagonals]

for l in diagonal_lines:
    xmas_count += l.count("XMAS")
    xmas_count += l.count("SAMX")

print(xmas_count)