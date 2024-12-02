import re

LINE_PATTERN = re.compile("Step (?P<dependency>\w) must be finished before step (?P<step>\w) can begin.")
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

file = open("day07/input.txt")
lines = [LINE_PATTERN.match(l.strip()).groupdict() for l in file.readlines()]

steps = dict([(s, []) for s in sorted(set([l['step'] for l in lines] + [l['dependency'] for l in lines]))])
for l in lines:
    steps[l['step']].append(l['dependency'])
    
ordering = ""
workers = []
for i in range(5):
    workers.append({ "current_step": None, "time_remaining": -1 })

time = -1
while steps:
    time += 1
    occupied = [w for w in workers if w["current_step"] is not None]
    free = [w for w in workers if w["current_step"] is None]
    
    for worker in occupied:
        if worker["time_remaining"] == 0:
            ordering += worker["current_step"]
            steps.pop(worker["current_step"])
            for s in steps:
                if worker["current_step"] in steps[s]:
                    steps[s].remove(worker["current_step"])
            worker["current_step"] = None
        else:
            worker["time_remaining"] -= 1
            
    
    available = [s for s in steps if len(steps[s]) == 0 and s not in [w["current_step"] for w in workers]]
    for worker in free:
        if len(available) > 0:
            next = available.pop(0)
            worker["current_step"] = next
            worker["time_remaining"] = 60 + LETTERS.index(next)
                
print(time)