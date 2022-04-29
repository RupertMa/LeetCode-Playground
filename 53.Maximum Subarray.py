from typing import List
from collections import defaultdict

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        if ans<=0:
            return ans
        cum_sum = 0
        max_sum = 0
        for num in nums:
            cum_sum += num
            cum_sum = max(0, cum_sum)
            max_sum = max(max_sum, cum_sum)
        return max_sum

        # Greedy algorithm
        # Time complexity: O(N)
        # Space complexity: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_num = max(nums)
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
            max_num = max(max_num, dp[i])
        return max_num

        # DP
        # Time complexity: O(N)
        # Space complexity: O(N)
