inp = input().split(" ")
n = int(inp[0])
m = int(inp[1])



with open("rez3.txt","w") as f:
    for i in range(n):
        inp = input().split(" ")
        r=int(inp[0][:-1])
        p=int(inp[1][:-1])
        s=int(inp[2][:-1])
        aux=""

        # while s>1 and p>0 and r>1:
        #     aux = aux +"SRRP"
        #     r-=2
        #     p-=1
        #     s-=1

        # while r > 2:
        #     aux = aux + "RRPR"
        #     r-=3
        #     p-=1

        while r>p and r > 0 and p > 0:
            aux = aux + "RR"
            r-=2
            if r<=p: break
            aux = aux+"PR"
            r-=1
            p-=1


        while r>0 and p>0:
            aux = aux+"PR"
            r-=1
            p-=1
        while p>s:
            aux = aux + "PP"
            p-=2
        while p>0 and s>0:
            aux = aux + "PS"
            s-=1
            p-=1
        while s>0:
            aux = aux + "S"
            s-=1
        print(r,p,s)

        caux = ""
        for i in range(0, m-3,4):
            vaux= aux[i]+aux[i+1]+aux[i+2]+aux[i+3]
            if "RRPS" in vaux:
                caux = caux + "RPRS"
            else:caux = caux + vaux

        f.write(aux+"\n")
