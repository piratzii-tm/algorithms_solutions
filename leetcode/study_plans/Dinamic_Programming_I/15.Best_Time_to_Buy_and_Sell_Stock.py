class Solution:
    def maxProfit(self, x: List[int]) -> int:
        profit = 0 
        minim = x[0]
        i = 0
        while i < len(x)-1:
            minim = min(minim, x[i])
            if x[i] <= minim:
                profitPerBuy = max(x[i+1:]) - x[i]
                profit = max(profit, profitPerBuy)
            if minim == 0: break
            i += 1
        return profit