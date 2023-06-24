class Solution:
    def countVowelStrings(self, n: int) -> int:
        sums = [1,1,1,1,1]
        for i in range(1,n):
            aux = []
            for j in range(5):
                aux.append(sum(x for x in sums[j:]))
            sums = aux
        return sum(x for x in sums)