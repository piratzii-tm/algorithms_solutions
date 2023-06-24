class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                ind = t.index(i)
                t = t[ind+1:]
            else: return False
        return True