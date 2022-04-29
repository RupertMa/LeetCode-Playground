class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0
        Sum = 0
        preSum2 = {}
        for i in range(len(A)):
            Sum += A[i]
            ans += len(preSum2.get(Sum%K,[]))
            preSum2[Sum%K] = preSum2.get(Sum%K,[]) + [Sum]
            if Sum % K == 0:
                ans += 1
        return ans

# Time complexity: O(N)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        preSum = 0
        seen = {0:1}
        for i, num in enumerate(nums):
            preSum += num
            if preSum % k in seen:
                    ans += seen[preSum%k]
            seen[preSum%k] = seen.get(preSum%k, 0) + 1
        return ans
