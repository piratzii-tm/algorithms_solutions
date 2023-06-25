class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0 
        maxs = 0
        for i in gain:
            alt = alt + i
            maxs = max(maxs,alt)
        return maxs