from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) ; n = len(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    continue

                if i !=0 and j!=0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i==0 and j!=0:
                    dp[i][j] = dp[i][j-1]
                elif i!=0 and j==0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = 1
        return dp[i][j]

    # Time complexity: O(N*M)
    # Space complexity: O(N*M)

    # Actually, space complexity can be optimized to O(N)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) ; n = len(obstacleGrid[0])
        dp = [[0]*n for i in range(2)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[i%2][j] = 0
                    continue

                if i !=0 and j!=0:
                    dp[i%2][j] = dp[(i-1)%2][j] + dp[i%2][j-1]
                elif i==0 and j!=0:
                    dp[i%2][j] = dp[i%2][j-1]
                elif i!=0 and j==0:
                    dp[i%2][j] = dp[(i-1)%2][j]
                else:
                    dp[i%2][j] = 1
        return dp[i%2][j]
