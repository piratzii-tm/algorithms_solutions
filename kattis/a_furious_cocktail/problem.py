inp = input().split(" ")
n = int(inp[0])
t = int(inp[1])

p = []

for i in range(n):
    p.append(int(input()))

p.sort(reverse=True)

potions = dict()
for i in range(len(p)):
    potions[i]=[t*(i+1),p[i]+t*(i+1)]

res = "YES"
for i in range(len(p)-1,-1,-1):
    st = potions[i][0]
    for j in range(i):
        ft = potions[j][1]
        if st>=ft:
            res = "NO"
            break
    if res == "NO":break

print(res)