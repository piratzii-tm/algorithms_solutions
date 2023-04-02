inp = input().split(" ")
n = int(inp[0])
m = int(inp[1])



with open("rez4.txt","w") as f:
    for i in range(n):
        inp = input().split(" ")
        r=int(inp[0][:-1])
        p=int(inp[1][:-1])
        s=int(inp[2][:-1])
        aux=""

        if r > 3:
            aux = aux + "RRRP"
            r -= 3
            p -= 1
            
        while r>=4:
            aux = aux + "RRRR"
            r-=4
        
        # -- p r<4
        print(r,p,s)
        
        # while p>0 and r>0:
        #     aux = aux + "PR"
        #     p-=1
        #     r-=1
        #     if p>1:
        #         aux= aux+"PP"
        #         p-=2
        #     elif 

        if r > 0:
            if p > 0:
                aux = aux + "RP"
                r -= 1
                p -= 1
            else:
                aux = aux + "RS"
                r -= 1
                s -= 1
            while r>0:
                aux = aux + "R"
                r-=1
        
        
        # if r>0:
        #     k=r
        #     while r>0:
        #         aux = aux+"R"
        #         r-=1
        #     while k<=4:
        #         aux = aux + "S"
        #         k+=1
        # gata cu r
        while p>0:
            aux = aux + "P"
            p-=1
        while s>0:
            aux = aux+"S"
            s-=1

        f.write(aux+"\n")
