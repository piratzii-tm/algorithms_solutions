def verif(res,strn):
    for i in range(len(strn)//2+1):
        if res*(i+1) == strn: return True
    return False

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        max = ""
        if verif(str2,str1): return str2
        if verif(str1,str2): return str1
        for i in str2:
            res += i
            if verif(res,str1) and verif(res,str2) and len(max)<len(res): max=res
        return max