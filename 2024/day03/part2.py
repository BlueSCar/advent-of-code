import re

INSTRUCT_PATTERN = re.compile("(mul|don't|do)\((?:(\d+),(\d+))?\)")

file = open("2024/day03/input.txt")
contents = file.read()
instructions = INSTRUCT_PATTERN.findall(contents)

enabled = True
total = 0

for i in instructions:
    if i[0] == "mul" and enabled:
        total += int(i[1]) * int(i[2])
    elif i[0] == "don't":
        enabled = False
    elif i[0] == "do":
        enabled = True

print(total)
