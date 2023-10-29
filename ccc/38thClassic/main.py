import copy

def dfs(grid, i, j, x, y):

    global rez
    if i == x and y == j:
        rez = True
        return 
    if i<0 or j<0 or i>= len(grid) or j >= len(grid[0]) or grid[i][j] != "L":
        return

    grid[i][j] = "W"
    dfs(grid, i+1, j,x,y)
    dfs(grid, i-1, j,x,y)
    dfs(grid, i, j+1,x,y)
    dfs(grid, i, j-1,x,y)

rez = False

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

    print(g)

    for i in g:
        rez = False
        aux  = copy.deepcopy(mat)
        dfs(aux,int(i[0][1]),int(i[0][0]), int(i[1][1]),int(i[1][0]))  
        if rez:
            f.write("SAME\n")
        else:
            f.write("DIFFERENT\n")
        
    f.close()
