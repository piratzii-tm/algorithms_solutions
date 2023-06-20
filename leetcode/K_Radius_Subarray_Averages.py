class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        resp = []
        if k == 0:
            resp = nums
        elif k > len(nums)+1:
            for i in range(len(nums)):
                resp = [-1]
        else:
            s = 0
            for i in range(len(nums)):
                
                if i < k: resp.append(-1)
                elif i+k >= len(nums): resp.append(-1)
                else:
                    if s == 0:
                        j = i-k
                        s = 0 
                        while j <= i+k:
                            s += nums[j]
                            j+=1
                    else:
                        s -= nums[i-k-1]
                        s += nums[i+k]
                    print(s)
                    resp.append(s//(2*k+1))

        return resp