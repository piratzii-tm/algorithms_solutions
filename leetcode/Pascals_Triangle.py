class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        v = [ [1 for j in range(numRows)] for i in range(numRows)]
        v[0] = [1 for i in range(numRows)]

        out = [[] for i in range(numRows)]

        for i in range(1, numRows):
            for j in range(1, numRows):
                if i+j<numRows: v[i][j] = v[i-1][j] + v[i][j-1]
        
        k = 0
        while k<numRows:
            i = k
            j = 0
            while i>=0:
                out[k].append(v[i][j])
                i-=1
                j+=1
            k+=1
        return out