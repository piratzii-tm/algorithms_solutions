class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        def calc(nr):
            s = 0
            for j in range(len(nums)):
                s += abs(nr-nums[j])*cost[j]
            return s
	
#FOLOSIM BS PENTRU A GASI ELEMENTUL CEL MAI OPTIM PENTRU A CONVERTI RESTUL ELEMENTELOR
        left = min(nums)
        right = max(nums)+1
        mid = (left + right)//2

        while left<right:
            if calc(mid) < calc(mid+1):
                right = mid
            else: left = mid+1
            mid = (left+right)//2
        
        return calc(left)