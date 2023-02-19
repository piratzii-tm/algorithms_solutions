class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        n = len(nums)
        lmax1 = lmax2 = 0

        p = 1
        k = 0 
        for i in range(n):

            p*=nums[i]
            k += 1

            if p>0 and lmax1<=k: 
                lmax1 = k

            if nums[i] == 0:
                p = 1
                k = 0
        
        p = 1
        k = 0
        for i in range(n-1,-1,-1):
            
            p*=nums[i]
            k += 1

            if p>0 and lmax2<=k:
                lmax2 = k
            
            if nums[i] == 0:
                p = 1
                k = 0

        print(lmax1,lmax2)
        return max(lmax1,lmax2)
        