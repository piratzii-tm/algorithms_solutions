def solution(n,v):
    if v[n]!=0:return v[n]
    elif n<3: v[n]=n
    else: v[n]=solution(n-1,v)+solution(n-2,v)
    return v[n]



class Solution:
    def climbStairs(self, n: int) -> int:
        v = [0 for i in range(n+1)]
        return solution(n,v)