#ne folosim de o variabila globala counter ca sa verificam numarul de parcele dintr-o insula care exista
#apoi o comparam cu numarul de parcele dintr-o insula care nu se afla la margine
#daca sunt egale atunci incrementam contorul k cu numarul de parcele corspunzator
#daca nu sunt egale, nu incrementam

counter = 0

def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
        return -1
    if grid[i][j] != 1: return 0
    
    global counter 
    counter += 1
    grid[i][j] = 0
    return 1 + dfs(grid,i-1,j) + dfs(grid,i,j-1) + dfs(grid,i+1,j) + dfs(grid,i,j+1)

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        global counter
        

        if not grid: return 0
        k=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                   a2 = dfs(grid,i,j)
                   a1 = counter
                   if a1==a2:k+=a2
                   counter = 0
        return k