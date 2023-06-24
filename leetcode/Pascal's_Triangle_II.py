class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 : return [1]
        if rowIndex == 1 : return [1,1]
        
        ans = [1,1]
        for i in range(2,rowIndex+1):
            aux = [1]
            for j in range(len(ans)-1):
                aux.append(ans[j]+ans[j+1])
            aux.append(1)
            ans = aux
        return ans