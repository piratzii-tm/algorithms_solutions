class Solution(object):
    def removeDuplicates(self, nums):
        maxim = max(nums) + 1
        for i in range(2, len(nums)):
            if (nums[0:i].count(nums[i]) >= 2):
                nums[i] = maxim
        nums.sort()
        print(nums)
        return len(nums) - nums.count(maxim)