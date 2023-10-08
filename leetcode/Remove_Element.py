class Solution(object):
    def removeElement(self, nums, val):
        x = 0
        for i in range(len(nums) - nums.count(val)):
            if(nums[i] == val):
                while nums[i]==val:
                    aux = nums[i]
                    nums[i] = nums[len(nums)-1-x]
                    nums[len(nums)-1-x] = aux
                    x+=1
                print(nums)
        return len(nums) - nums.count(val)