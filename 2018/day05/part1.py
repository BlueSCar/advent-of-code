lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

file = open("day05/input.txt")
chain = file.read()

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

print(len(chain))