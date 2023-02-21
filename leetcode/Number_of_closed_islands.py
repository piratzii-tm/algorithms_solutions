def dfs(grid, i, j):
    #verificam daca parcela de insula se afla la margine
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
        return -1 #daca da returnam -1

    #altfel returnam 0 indiferent de caz
    if grid[i][j] != 0: return 0

    grid[i][j] = 1
    return 0 + dfs(grid,i+1,j) + dfs(grid,i,j+1) + dfs(grid,i-1,j) + dfs(grid,i,j-1)

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        if not grid: return 0

        k = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    k += 1 
                    #incrementam un contor si daca insula se afla la margine
                    #adica nu este inconjurata de apa
                    if dfs(grid,i,j) != 0:
                        k -= 1 #daca se afla la margine decrementam contorul
        return k