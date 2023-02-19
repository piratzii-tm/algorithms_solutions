#procesare input
with open("input.txt","r") as f:
    inp = f.readline().split(" ")
    F = []
    B = []
    for i in range(0,len(inp),3):
        if inp[i] == "F":
            F.append((int(inp[i+1]),int(inp[i+2])))
        else:
            B.append((int(inp[i+1]),int(inp[i+2])))

with open("output.txt","w") as f:
    for i in range(len(F)):
        if F[i][1] > B[i][1]:
            f.write(str(F[i][0])+" ")

#levelul 2 e acelasi cu 1 doar ca are inputuri mai mari