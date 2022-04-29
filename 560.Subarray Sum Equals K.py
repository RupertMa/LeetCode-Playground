from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        dmap = {0:[-1]}
        Sum = 0
        for i,n in enumerate(nums):
            Sum += n
            m = Sum - k
            if m in dmap:
                ans += len(dmap[m])
            dmap[Sum] = dmap.get(Sum,[]) + [i]
        return ans

        # Time complexity: O(N)
        # Space complexity: O(N)

    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        preSum = 0
        dmap = {0:1}
        for i, n in enumerate(nums):
            preSum += n
            m = preSum - k
            if m in dmap:
                ans += dmap[m]
            dmap[preSum] = dmap.get(preSum, 0) + 1
        return ans
        # Time complexity: O(N)
        # Space complexity: O(unique preSum)
        # Faster than list append
