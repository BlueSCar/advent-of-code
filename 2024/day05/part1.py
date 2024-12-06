file = open("2024/day05/input.txt")

contents = file.read()
rules = [tuple(map(int, r.split('|'))) for r in contents.split("\n\n")[0].split("\n")]
updates = [list(map(int, u.split(','))) for u in contents.split("\n\n")[1].split("\n")]

middles = []

for pages in updates:
    is_correct = True
    for i in range(len(pages)):
        for rule in rules:
            if rule[0] == pages[i]:
                if rule[1] in pages[:i]:
                    is_correct = False
                    break
            elif rule[1] == pages[i]:
                if rule[0] in pages[i+1:]:
                    is_correct = False
                    break
                
        if not is_correct:
            break
    if is_correct:
        middles.append(pages[int(len(pages)/2)])

print(sum(middles))