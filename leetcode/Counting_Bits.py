def binrep(n):
    k = 0
    while n:
        if n%2 == 1: k+=1
        n//=2
    return k
    
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(binrep(i))
        return ans