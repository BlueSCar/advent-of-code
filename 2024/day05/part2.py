file = open("2024/day05/input.txt")

contents = file.read()
rules = [tuple(map(int, r.split('|'))) for r in contents.split("\n\n")[0].split("\n")]
updates = [list(map(int, u.split(','))) for u in contents.split("\n\n")[1].split("\n")]

def is_disorded(pages: list[int], rules: tuple[int]):
    for i in range(len(pages)):
        for rule in rules:
            if rule[0] == pages[i]:
                if rule[1] in pages[:i]:
                    return True
            elif rule[1] == pages[i]:
                if rule[0] in pages[i+1:]:
                    return True
                
    return False

def order_pages(pages: list[int], rules: tuple[int]):
    new_pages = pages.copy()
    for i in range(len(pages)):
        for rule in rules:
            new_index = new_pages.index(pages[i])
            if rule[0] == pages[i]:
                if rule[1] in new_pages[:new_index]:
                    new_pages.remove(rule[1])
                    new_pages.insert(new_index, rule[1])
            elif rule[1] == pages[i]:
                if rule[0] in new_pages[new_index+1:]:
                    new_pages.remove(rule[0])
                    new_pages.insert(new_index+1, rule[0])
                
    if not is_disorded(new_pages, rules):
        return new_pages
    else:
        return order_pages(new_pages, rules)

corrected_sets = []
for update in updates:
    if is_disorded(update, rules):
        corrected = order_pages(update, rules)
        corrected_sets.append(corrected)
        
total = sum([corrected[int(len(corrected)/2)] for corrected in corrected_sets])

print(total)