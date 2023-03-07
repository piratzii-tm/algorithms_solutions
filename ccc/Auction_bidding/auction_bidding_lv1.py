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
max = d
b=""
p=1
for i in l:
    if i[1]>p: 
        b = i[0]
        d = p+1
        p = i[1]
        
    elif i[1]<p: 
        d = i[1]+1
    else: d = i[1]
print("{},{}".format(b,d))