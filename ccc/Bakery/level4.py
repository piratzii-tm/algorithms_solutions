#la fel ca la levelul 3 dar nu luam toate numerele ci doar pana la maximul zilei in care se poate plati

from itertools import combinations

#procesare input
with open("input.txt","r") as f:
    inp = f.readline().split("F")
    B = inp[len(inp)-1].split("B")
    F = inp[1:len(inp)-1:]
    F.append(B[0])
    B = B[1:]

    aux = []
    for i in F:
        i = i.split(" ")
        aux2 = []
        for j in i:
            try:
                aux2.append(int(j))
            except: continue
        aux.append(aux2)
    F=aux

    aux = []
    for i in B:
        i = i.split(" ")
        aux2 = []
        for j in i:
            try:
                aux2.append(int(j))
            except: continue
        aux.append(aux2)
    B=aux


with open("output.txt","w") as f:
    
    for x in range(len(F)):

        string = [B[j][1] for j in range(len(B)) if (B[j][0]<=(F[x][1]+F[x][0]-1) and B[j][1]<=F[x][2])]
        string.sort()

        ok = True
        for i in range(0,len(string)+1):
            for element in combinations(string,i):
                s = sum( element[i] for i in range(len(element)))
                print(F[x][2],"verif",element)
                if s == F[x][2]:
                    ok = False
                    break
                if s>F[x][2]:break
            if s>F[x][2]:break
                
        
        if ok:
            f.write(str(F[x][0])+" ")
        

        



