class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A)
        m = len(A[0])
        ans = 0
        for i in range(m):
            count = True
            for j in range(1,n):
                if A[j-1][i] > A[j][i]:
                    count = False
                    break
            if count:
                ans += 1
        return m - ans
        