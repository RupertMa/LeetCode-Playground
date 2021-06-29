class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1, 1]
        k = 2
        while k <= n:
            ans[k%2] = sum(ans)
            k += 1
        return ans[n%2]

    # Time complexity: O(N)
