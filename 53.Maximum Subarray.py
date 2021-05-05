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
