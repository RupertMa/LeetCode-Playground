class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        from collections import Counter
        dp = Counter()
        dp[0] = 1
        for num in nums:
            ndp = Counter()
            for sign in [-1,+1]:
                for key in dp.keys():
                    ndp[key + num * sign] += dp[key]
            dp = ndp
        return dp[S]
            