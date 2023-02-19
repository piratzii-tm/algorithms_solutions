def minim(x,y):
    if x<y: y=x
    return y

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        minCost = [0,cost[0]]
        for i in range(2,n+1):minCost.append(0)
        for i in range(2,n+1):
            minCost[i] = cost[i-1] + min(minCost[i-1],minCost[i-2])
        return minim(minCost[n],minCost[n-1])