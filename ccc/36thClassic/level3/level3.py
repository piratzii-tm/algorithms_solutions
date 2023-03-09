n = int(input())
board=[]
for i in range(n):
    rand = []
    s=input()
    for j in s:
        rand.append(j)
    board.append(rand)

pacman = input().split(" ")
px = int(pacman[0])-1
py = int(pacman[1])-1

seqLength = int(input())
inp = input()
pcm_moves = []
for i in inp:
    pcm_moves.append(i)

phtNr = int(input())
pht = dict()
for i in range(phtNr):
    inp = input().split(" ")
    fx = int(inp[0])-1
    fy = int(inp[1])-1
    aux = int(input())
    inp = input()
    f_moves = []
    for j in inp:
        f_moves.append(j)
    
    pht[i]= []
    pht[i].append([fx,fy])
    pht[i].append(f_moves)

def move(x,y,dir):
    if dir == 'R':y += 1
    elif dir == 'L':y-=1
    elif dir == 'D':x+=1
    elif dir == 'U':x-=1

    return x,y

def gameplay(px, py, pht):
    coins = 0
    for i in range(seqLength):
        #pacman coord change
        px,py = move(px,py,pcm_moves[i])
        for j in pht:
            #ph coord change
            fx = pht[j][0][0]
            fy = pht[j][0][1]
            dir = pht[j][1][i]
            fx,fy = move(fx,fy,dir)
            pht[j][0][0] = fx
            pht[j][0][1] = fy

            #verify
            if px == fx and py == fy: return coins,"NO"
        
        if board[px][py]=='W': return coins,"NO"
        elif board[px][py]=='C': 
            coins+=1
            board[px][py]="N"
    return coins,"YES"

print(gameplay(px,py,pht))