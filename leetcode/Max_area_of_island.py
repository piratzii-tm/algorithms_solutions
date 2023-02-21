#foarte asemanatoare cu number of islands 
# doar ca in loc sa incrementam un contor in momentul in care gasim o insula, 
# numaram fiecare parcela din insula respectiva si vedem care e cea mai mare

def dfs(grid, i, j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1: return 0
    grid[i][j] = 0
    return 1+dfs(grid,i+1,j)+dfs(grid,i,j+1)+dfs(grid,i-1,j)+dfs(grid,i,j-1)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid: return 0
        max = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    k = dfs(grid,i,j)
                    if k > max: max = k
        return max