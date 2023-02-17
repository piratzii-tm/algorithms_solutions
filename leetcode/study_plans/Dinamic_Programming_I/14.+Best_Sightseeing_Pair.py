#This solution is of the complexity O(n**2) so not all the testcases passed 43/54

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        resp = 0
        i = 0
        while i < len(values)-1:
            j = i+1
            while j < len(values):
                score = values[i] + i + values[j] - j
                if score > resp: resp = score
                j+=1
            i+=1
        return resp 