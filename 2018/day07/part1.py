import re

LINE_PATTERN = re.compile("Step (?P<dependency>\w) must be finished before step (?P<step>\w) can begin.")

file = open("day07/input.txt")
lines = [LINE_PATTERN.match(l.strip()).groupdict() for l in file.readlines()]

steps = dict([(s, []) for s in sorted(set([l['step'] for l in lines] + [l['dependency'] for l in lines]))])
for l in lines:
    steps[l['step']].append(l['dependency'])
    
ordering = ""
while steps:
    next = [s for s in steps if len(steps[s]) == 0][0]
    ordering += next
    steps.pop(next)
    for s in steps:
        if next in steps[s]:
            steps[s].remove(next)

print(ordering)