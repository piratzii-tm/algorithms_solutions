class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        v = [ [ 0 for j in range(n)] for i in range(m)]

        for j in range(n):
            if obstacleGrid[0][j] == 1: break
            else: v[0][j] = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1: break
            else: v[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1: v[i][j] = 0
                else: v[i][j] = v[i-1][j] + v[i][j-1]
        return v[m-1][n-1]