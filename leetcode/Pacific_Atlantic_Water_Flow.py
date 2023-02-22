class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])

        s = [ [0 for i in range(n)] for j in range(m)]
        k = 1

        res = []

        for i in range(m):
            for j in range(n):
                q=[(i,j)]
                s[i][j] = k
                po = False
                ao = False
                if i==0 or j==0:po=True
                if i==m-1 or j==n-1:ao=True
                while q:
                    r0,c0 = q[0]
                    q = q[1:]

                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):

                        r1,c1 = r0+dr,c0+dc
                        if 0<=r1<m and 0<=c1<n and heights[r1][c1]<=heights[r0][c0] and s[r1][c1]!=k:
                            s[r1][c1]=k
                            q.append((r1,c1))
                            if r1 == 0 or c1==0: po=True
                            if r1 == m-1 or c1 == n-1: ao=True
                if po and ao: res.append([i,j])
                k+=1
        return res

                 