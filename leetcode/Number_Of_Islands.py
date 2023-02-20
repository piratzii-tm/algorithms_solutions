#48/49 test cases past

def corect(s):
    for i in s:
        for j in i:
            if j == "1": return True
    return False

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        isl = 0
        sx = 0
        sy = 0
        while corect(grid):
            ok = False
            #verific prima pozitie posibila
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        sx = i
                        sy = j
                        ok = True
                        break
                if ok:break
            if sx==-1 or sy == -1: return isl
            #daca exista vedem insula cu Lee
            if sx!=-1 and sy!=-1:
                q = [ [sx,sy] ]
                grid[sx][sy] = "0"
                while len(q)!=0:
                    X = q[0][0]
                    Y = q[0][1]
                    if X-1>=0 and grid[X-1][Y] == "1":
                        q.append([X-1,Y])
                        grid[X-1][Y] = "0"
                    if X+1<len(grid) and grid[X+1][Y] == "1":
                        q.append([X+1,Y])
                        grid[X+1][Y] = "0" 
                    if Y-1>=0 and grid[X][Y-1] == "1":
                        q.append([X,Y-1])
                        grid[X][Y-1] = "0"
                    if Y+1<len(grid[0]) and grid[X][Y+1] == "1":
                        q.append([X,Y+1])
                        grid[X][Y+1] = "0"
                    q=q[1:]
            isl+=1
        return isl



