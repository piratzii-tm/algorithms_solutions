class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
       	n = len(nums)

        frecv = [ 0  for i in range(max(nums)+1)]
        frecv[0] = 0
        for i in nums: frecv[i] += i

        s = [0 for i in range(len(frecv))]

        s[0] = 0
        s[1] = frecv[1]

        for i in range(2,len(frecv)):
            s[i] = max(frecv[i]+s[i-2], s[i-1])

        return s[len(frecv)-1]
#Ideea este ca in loc sa ne folosim de numerele propriu zise ne folosim de frecventa lor reducand lungimea sirului.
#Spre exemplu in loc sa folosim sirul 8 10 4 9 1 3 5 9 4 10, folosim sirul de frecvente unde fiecare element este egal cu suma elementelor pozitiei (exemplu frcv[9]=18 -> 2*9) deci frcv = [0,1,0,3,8,5,0,8,18,29]. Iar pe acest si folosim House Robber 