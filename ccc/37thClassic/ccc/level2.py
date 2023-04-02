inp = input().split(" ")
n = int(inp[0])
m = int(inp[1])

with open("rez2.txt", "w") as f:
    for j in range(n):
        s = input()
        k =0
        while k!=2:
            aux=""
            for i in range(0, len(s)-1, 2):
                cs = ""
                cs=cs+s[i]
                cs=cs+s[i+1]
                if cs=="SP" or cs=="PS": aux=aux+"S"
                elif cs=="RS" or cs=="SR": aux=aux+"R"
                elif cs=="RP" or cs=="PR": aux=aux+"P"
                elif cs[0]==cs[1]:aux=aux+cs[0]
            s = aux
            k+=1
        f.write(s+"\n")