n = int(input())
m=[]
for i in range(n):
    rand = []
    s=input()
    for j in s:
        rand.append(j)
    m.append(rand)

pacman = input().split(" ")
px = int(pacman[0])-1
py = int(pacman[1])-1

k = int(input())
s = input()
l = []
for i in s:
    l.append(i)

coins = 0
for i in l:
    if i == 'R':py += 1
    elif i == 'L':py-=1
    elif i == 'D':px+=1
    elif i == 'U':px-=1

    if m[px][py]=='C':
        coins+=1
        m[px][py]='N'


print(coins)

