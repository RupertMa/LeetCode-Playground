class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(target):
            for j in range(n):
                if nums[j] + i <= target:
                    dp[nums[j] + i] += dp[i]
        return dp[target]