class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        s = [0 for i in range(n)]
        s[0] = nums[0]
        for i in range(1,n):
            max = 0
            for j in range(1,i-1):
                if s[j]>max:max=s[j]
            s[i] = max + nums[i]

        max1 = 0 
        for i in range(n):
            if max1<s[i]:max1 = s[i]
        
        s = [0 for i in range(n)]
        s[0] = nums[0]
        for i in range(1,n-1):
            max = 0
            for j in range(0,i-1):
                if s[j]>max:max=s[j]
            s[i] = max + nums[i]

        max2 = 0 
        for i in range(n):
            if max2<s[i]:max2 = s[i]

        if max1<max2:max1=max2
        return max1
        


