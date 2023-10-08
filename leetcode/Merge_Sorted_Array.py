class Solution(object):
    def merge(self, nums1, m, nums2, n):
        aux = [0 for i in range(m + n)]

        i = 0
        j = 0
        k = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                aux[k] = nums1[i]
                i += 1
                k += 1
            else:
                aux[k] = nums2[j]
                j += 1
                k += 1

        while i < m:
            aux[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            aux[k] = nums2[j]
            j += 1
            k += 1

        for num in range(n + m):
            nums1[num] = aux[num]

