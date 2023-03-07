inp = input()
u = inp.index(",")
d=int(inp[0:u])
inp = inp[u+1:]
print(inp)
s = inp.split(",")
l = []

for i in range(0,len(s),2):
    x = int(s[i+1])
    l.append((s[i],x))
b=""
p=1
h = ['-',',',d,","]
for i in l:
    cd = d
    if i[1]>p and i[0]==b: 
        p =i[1]
    elif i[1]>p: 
        b = i[0]
        d = p+1
        p = i[1]
    elif i[1]<p: 
        d = i[1]+1
    else: d = i[1]
    
    if d!=cd:
        h.append(b)
        h.append(",")
        h.append(d)
        h.append(",")
print("{},{}".format(b,d))
for i in h[:-1]:print(i,end="")