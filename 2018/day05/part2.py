lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

file = open("day05/input.txt")
input = file.read()

def react(chain):
    found = True
    while found:
        found = False
        for i in range(26):
            pair1 = f"{lowers[i]}{uppers[i]}"
            pair2 = f"{uppers[i]}{lowers[i]}"
            
            new_chain = chain.replace(pair1, "").replace(pair2, "")
            if len(new_chain) < len(chain):
                found = True
                chain = new_chain

    return len(chain)
    
shortest = 1e100
for i in range(26):
    length = react(input.replace(lowers[i], "").replace(uppers[i], ""))
    if length < shortest:
        shortest = length
        
print(shortest)