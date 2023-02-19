from itertools import combinations

#procesare input
with open("input.txt","r") as f:
    inp = f.readline().split(" ")
    F = []
    B = []
    for i in range(0,len(inp),3):
        if inp[i] == "F":
            F.append((int(inp[i+1]),int(inp[i+2])))
        else:
            B.append([int(inp[i+1]),int(inp[i+2])])

M = []
with open("output.txt","w") as f:
    
    string = [B[i][1] for i in range(len(B))]

    for i in range(0,5):
        for element in combinations(string,i):
            s = sum( element[i] for i in range(len(element)))
            M.append(s)

    for i in range(len(F)):
        if F[i][1] not in M:
            f.write(str(F[i][0])+" ")



