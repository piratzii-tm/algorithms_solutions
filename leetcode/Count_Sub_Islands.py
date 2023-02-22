def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1: return

    grid[i][j] = "#"
    dfs(grid,i+1,j)
    dfs(grid,i,j+1)
    dfs(grid,i-1,j)
    dfs(grid,i,j-1)

counter = 0

def verif(grid1,grid2,i,j):
    if i<0 or j<0 or j>=len(grid2[0]) or i>=len(grid2) or grid2[i][j] != 1: return 0

    global counter

    if grid1[i][j] == "#": counter+=1
    grid2[i][j] = 0
    return 1 + verif(grid1,grid2,i-1,j) + verif(grid1,grid2,i,j-1) + verif(grid1,grid2,i+1,j) + verif(grid1,grid2,i,j+1)

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        if not grid1 or not grid2: return 0
        k = 0
        global counter

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 1:
                    dfs(grid1,i,j)

        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    x = verif(grid1,grid2,i,j)
                    if x == counter: k+=1
                    counter = 0
        return k
