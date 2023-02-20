class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        v = [ [0 for j in range(n)] for i in range(m)]

        for j in range(n): v[0][j] = 1
        for i in range (m): v[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                v[i][j] = v[i-1][j] + v[i][j-1]
        
        return v[m-1][n-1]  