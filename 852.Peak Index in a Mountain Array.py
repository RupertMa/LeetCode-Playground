class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 0
        r = len(A) - 1
        while l <= r:
            median = (l + r) // 2
            if A[median] > A[median-1]:
                l = median + 1
            else:
                r = median - 1
        return l-1
         