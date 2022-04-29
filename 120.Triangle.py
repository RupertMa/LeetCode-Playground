class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0]]
        for i in range(1, len(triangle)):
            n = len(triangle[i])
            temp = [0] * n
            temp[0] = dp[0] + triangle[i][0]
            temp[n-1] = dp[n-2] + triangle[i][n-1]
            for j in range(1, n-1):
                temp[j] = min(dp[j], dp[j-1]) + triangle[i][j]
            dp = temp
        return min(dp)
