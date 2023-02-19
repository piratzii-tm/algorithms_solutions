def alg(r1,c1,r2,c2,m,s,i):
    if m[r1][c1] == 1: 
        res = "decimal"
    else:
        res = "binary"

    if m[r1][c1] != m[r2][c2]: return "neither" #daca nu corespund coordonatele de start cu cele de finish

    if s[r1][c1] == 0: #daca nu s-a mai pornit de pe coordonatele respective:
        q = [[r1,c1]] # creem un queue nou si verificam daca avem drum pana la coordonatele de finish folosind algotritmul lui Lee
        while(len(q)!=0):
            X = q[0][0]
            Y = q[0][1]
            s[X][Y] = i
            
            if X-1>=0 and m[X-1][Y]==m[r1][c1] and s[X-1][Y]!=i: 
                q.append([X-1,Y])
                s[X-1][Y]=i
            if X+1<r and m[X+1][Y]==m[r1][c1] and s[X+1][Y]!=i: 
                q.append([X+1,Y]) 
                s[X+1][Y]=i
            if Y-1>=0 and m[X][Y-1]==m[r1][c1] and s[X][Y-1]!=i: 
                q.append([X,Y-1]) 
                s[X][Y-1]=i
            if Y+1<c and m[X][Y+1]==m[r1][c1] and s[X][Y+1]!=i: 
                q.append([X,Y+1])  
                s[X][Y+1]=i
            q = q[1:]
    #daca s-a m-ai pornit de pe coordonatele respective de start inseamna ca deja am verificat daca avem drum deoarece drumurile pot fi doar pe carare de 1 sau 0 
    if s[r1][c1] == s[r2][c2]:
        return res
    return "neither"



#procesam inputul  
inp = input().split(" ")
r = int(inp[0]) #numarul liniilor -- rows
c = int(inp[1]) #numarul coloanelor -- colums

m = [] # map
for i in range(r):
    row = input()
    m.append([int(j) for j in row])

n = int(input())
s = [ [ 0 for j in range(c)] for i in range(r)]
out = []
for i in range(n):
    x = input().split(" ")
    out.append(alg(int(x[0])-1,int(x[1])-1,int(x[2])-1,int(x[3])-1,m,s,i+1))

for i in out:print(i)