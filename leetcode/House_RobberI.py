class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0 for i in range(n)]
        s[0] = nums[0]
        for i in range(1,n):
            max = 0
            for j in range(0,i-1):
                if s[j]>max:max=s[j]
            s[i] = max + nums[i]

        max = 0 
        for i in range(n):
            if max<s[i]:max = s[i]
        
        return max