class Solution(object):
    def removeDuplicates(self, nums):
        myset = sorted(set(nums))
        k = 0
        for i in myset:
            nums[k] = i
            k += 1
        return len(myset)
