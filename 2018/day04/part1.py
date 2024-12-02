import re
from collections import Counter

RECORD_PATTERN = re.compile("\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (.+)")
SHIFT_PATTERN = re.compile("Guard #(\d+) begins shift")

def parse_record(line):
    g = RECORD_PATTERN.match(line).groups()
    ts = re.sub("\D", "", g[0])
    
    return (ts, g[1])

file = open("day04/input.txt")
records = sorted([parse_record(l.strip()) for l in file.readlines()], key=lambda record: record[0])

guards = {}
current_guard = None
start = 0
end = 0

for record in records:
    m = SHIFT_PATTERN.match(record[1])
    if m:
        current_guard = m.groups()[0]
        if current_guard not in guards:
            guards[current_guard] = []
    elif record[1] == "falls asleep":
        start = int(record[0][-2:])
    elif record[1] == "wakes up":
        end = int(record[0][-2:])
        guards[current_guard].extend(range(start, end))
        
sleepiest_guard = sorted(guards.items(), key=lambda g: len(g[1]))[-1]
c = Counter(sleepiest_guard[1]).most_common()[0]

print(int(sleepiest_guard[0]) * c[0])