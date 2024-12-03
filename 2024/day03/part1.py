import re

INSTRUCT_PATTERN = re.compile("mul\((\d+),(\d+)\)")

file = open("2024/day03/input.txt")
contents = file.read()
instructions = [tuple(map(int, i)) for i in INSTRUCT_PATTERN.findall(contents)]

total = sum([i[0] * i[1] for i in instructions])

print(total)
