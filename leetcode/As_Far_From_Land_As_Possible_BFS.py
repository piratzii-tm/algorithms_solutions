class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        #creem un queue in care adaugam prima data toate parcelele de pamant 
        q = [ (i,j) for i in range(n) for j in range(n) if grid[i][j]==1]
        maxim = 0

        while q:
            # r0 si c0 retin coordonatele primului element din q
            r0, c0 = q[0]
            # apoi stergem acel element din q
            q = q[1:]

            #dr- direction row si dc- direction column le folosim pentru a verifica vecinii
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):

                r1,c1 = r0+dr,c0+dc
                
                #daca vecinul se afla intre marginile grid-ului si este 0 atunci
                #il adaugam la q si valoarea din grid creste cu 1 simbolizand distanta de la acesta 
                #pana la cea mai apropiata parcela de pamant
                if 0<=r1<n and 0<=c1<n and not grid[r1][c1]:
                    q.append((r1,c1))
                    grid[r1][c1] = grid[r0][c0] + 1
                    maxim = max(maxim, grid[r1][c1])
        #returnam maxim-1 deoarece pornim de pe o parcela cu valoarea 1 nu 0
        return maxim-1


