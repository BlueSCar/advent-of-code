file = open('day3/input.txt')
lines = [l.strip() for l in file.readlines()]

counts = [sum(int(line[i]) for line in lines) for i in range(len(lines[0]))]

def get_gamma(digit):
    if digit > 500:
        return "1"
    else:
        return "0"

gammas = int("".join([get_gamma(c) for c in counts]), 2)
epsilons = int("".join([get_gamma(1000 - c) for c in counts]), 2)

print(gammas * epsilons)