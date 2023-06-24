def maximus(n):
    if n == 0 or n == 1: return n
    if n%2==0:
        return maximus(n//2)
    else: return maximus((n-1)//2) + maximus((n+1)//2)

class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        maxim = 0
        for i in range(n+1):
            maxim = max(maxim, maximus(i))
        return maxim