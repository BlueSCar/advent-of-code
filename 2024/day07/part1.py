file = open('2024/day07/input.txt')
lines = [dict(
    solution=int(l.split(":")[0].strip()),
    terms = [int(x.strip()) for x in l.split(":")[1].strip().split(" ")]
    ) for l in file.readlines()]

def is_valid(solution, current_solution, terms):
    if len(terms) == 1:
        return current_solution + terms[0] == solution or current_solution * terms[0] == solution
    else:
        return is_valid(solution, current_solution + terms[0], terms[1:]) or is_valid(solution, current_solution * terms[0], terms[1:])

sum = 0
for line in lines:
    if (is_valid(line['solution'], line['terms'][0], line['terms'][1:])):
        sum += line['solution']

print(sum)