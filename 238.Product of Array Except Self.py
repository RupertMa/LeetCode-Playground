class Solution:
    # Time complexity: O(N)
    # Space complexity: O(1) The output array does not count as extra space for the purpose of space complexity analysis.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        left = 1; right = 1
        for i in range(n-1):
            left *= nums[i]
            ans[i+1] *= left
        for i in range(n-1,0,-1):
            right *= nums[i]
            ans[i-1] *= right
        return ans