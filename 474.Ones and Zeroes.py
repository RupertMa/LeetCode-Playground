class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for i in range(m+1)]
        for s in strs:
            zero, one = s.count('0'), s.count('1')
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i - zero][j - one] + 1, dp[i][j])
        return dp[m][n]
