class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s = [1 for i in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    s[i] = max(s[j]+1,s[i])

        return max(i for i in s)