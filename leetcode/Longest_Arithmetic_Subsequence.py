class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        longest = 2

        # cd = common diff = diferenta dintre elemente/ratia    

        # o lista de dictionare
        # fiecare dictionar in parte retine nr de elemente care au cd la fel
        dp = [{} for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                # calculam diferenta
                diff = nums[i] - nums[j]

                # pentru fiecare diferenta din setul i cautam in seturile de la 0 la i-1 aceeasi diferenta si ii adaugam un 1, daca nu exista punem default 1
                dp[i][diff] = dp[j].get(diff, 1) + 1

                #retinem maximul la fiecare pas
                longest = max(longest, dp[i][diff])

        return longest