from typing import List

class Solution:
    # Time complexity: n
    def maxRotateFunction(self, A: List[int]) -> int:
        n = len(A)
        ans = val = sum(i*n for i, n in enumerate(A))
        Sum = sum(A)
        for i in range(n-1):
            val += n * A[i] - Sum
            ans = max(val, ans)
        return ans 

