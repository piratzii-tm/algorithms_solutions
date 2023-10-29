import copy

with open("output.txt", "w+") as f:
    
    n = int(input())
    mat = []
    f
    for i in range(n):
        mat.append(list(input()))

    m  = int(input())
    g = []
    for i in range(m):
        x = input()
        x = x.split(" ")
        x = [i.split(",") for i in x]
        g.append(x)


    for i in range(len(g)):
        for j in range(len(g[i])):
            for y in range(len(g[i][j])):
                g[i][j][y] = int(
                g[i][j][y]
                )

    for el in g:
        rez = False
        aux  = copy.deepcopy(mat)

        aux[el[0][1]][el[0][0]] = 0
        for poz in range(1,len(el)):
            prev = aux[el[poz-1][1]][el[poz-1][0]]
            curr = aux[el[poz][1]][el[poz][0]]

            if curr == 0: 
                rez = True 
                break

            if el[poz-1][1] - el[poz][1] !=0 and el[poz-1][0] - el[poz][0] !=0:
                #diag
                diffi = el[poz-1][1] - el[poz][1]
                diffj = el[poz-1][0] - el[poz][0]

                if aux[el[poz][1]+diffi][el[poz][0]] == 0 and aux[el[poz][1]][el[poz][0]+diffj] == 0:
                    #inters
                    rez = True
                    break
            aux[el[poz][1]][el[poz][0]] = 0

        if rez:
            f.write("INVALID\n")
        else:
            f.write("VALID\n")


        
    f.close()
