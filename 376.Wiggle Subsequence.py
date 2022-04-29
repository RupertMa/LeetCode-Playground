class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return size
        delta = nums[1] - nums[0]
        ans = 1 + (delta != 0)
        for i in range(2, size):
            new_delta = nums[i] - nums[i-1]
            if new_delta != 0 and delta * new_delta <= 0:
                ans += 1
                delta = new_delta
        return ans
    # Time complexity: O(N)
