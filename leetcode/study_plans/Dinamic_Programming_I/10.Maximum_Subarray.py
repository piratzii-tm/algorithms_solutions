class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0 for i in range(n)]

        s[0] = nums[0]
        max = s[0]

        for i in range(1,n):
            if s[i-1] + nums[i] < nums[i]: s[i] = nums[i]
            else: s[i] = s[i-1]+nums[i]

            if max < s[i]: max = s[i]
        
        return max