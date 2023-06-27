class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # res = []
        
        # for i in nums1:
        #     for j in nums2:
        #         heapq.heappush(res,(i+j,[i,j]))

        #         if len(res) > k:
        #             res.sort()
        #             res = res[:k]
        

        # return [res[i][1] for i in range(len(res))]

        res = []
        
        n = len(nums1)
        m = len(nums2)
        visited = set()

        if n == 0 or m == 0: return []
    
        h = [ (nums1[0]+nums2[0], (0,0)) ]

        for x in range(min(k,n*m)):

            non, (i,j) = heappop(h)
            res.append([nums1[i],nums2[j]])

            if i+1<n and (i+1,j) not in visited:
                heappush(h, (nums1[i+1]+nums2[j],(i+1,j)))
                visited.add((i+1,j))
            
            if j+1<m and (i,j+1) not in visited:
                heappush(h, (nums1[i]+nums2[j+1],(i,j+1)))
                visited.add((i,j+1))
            

        return res

        