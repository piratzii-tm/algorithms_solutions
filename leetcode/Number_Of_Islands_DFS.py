#dfs - deep first search
#aceasta este a doua rezolvare pentru aceeasi problema
#dfs functioneaza asemenator cu algoritmul lui Lee, poate chiar este la fel
def dfs(grid, i, j):
    #verificam daca este o posibilitate ca elementul sa sara din matrice
    if i<0 or j<0 or i>= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":return #daca da iesim  din functie, inseamna ca suntem la o margine
    #daca nu continuam sa verificam cat de mare este insula
    grid[i][j] = "0"
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        k = 0
        if not grid: return k

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #cautam sa vedem daca exista insula, daca da vedem cat de mare este
                if grid[i][j] == "1":
                    dfs(grid,i,j)
                    k+=1
        return k
#diferenta intre algoritmul acesta si celalalt este ca aici nu ne mai folosim de list q, doar marcam elementele cum ca am fost acolo