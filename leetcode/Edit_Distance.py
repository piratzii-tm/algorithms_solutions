class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #creeam o matrice in care la fiecare pas este evidentiata diferenta dintre cuvant word1[0..i] si word2[0..j]

        n = len(word1)+1
        m = len(word2)+1

        mat = [[0 for j in range(m)] for i in range(n) ]
        for i in range(m):
            mat[0][i] = i
        for i in range(n):
            mat[i][0] = i

        
        for i in range(1,n):
            for j in range(1,m):
                if word1[i-1] == word2[j-1]:
                    mat[i][j] = mat[i-1][j-1]
                else:
                    mat[i][j] = min(mat[i-1][j-1], mat[i-1][j], mat[i][j-1])+1
        
        return mat[n-1][m-1] 

