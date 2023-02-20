class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        MAX1 = MAX2 = nums[0]
        p=1
        for i in range(n):
            p *= nums[i]
            MAX1 = max(p,MAX1)
            if nums[i] == 0: p = 1

        p=1
        for i in range(n-1,-1,-1):
            p *= nums[i]
            MAX2 = max(p,MAX2)
            if nums[i] == 0: p = 1


        return max(MAX1,MAX2)
