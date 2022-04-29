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

    # Time complexity: O(N)
    # Space complexity: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = []
        ans = []
        for i, num in enumerate(nums):
            if num:
                product *= num
                all_zero = False
            else:
                zeros.append(i)
        if len(zeros) > 1:
            return [0] * len(nums)
        elif len(zeros) == 1:
            ans = [0] * len(nums)
            ans[zeros[0]] = int(product)
            return ans

        for num in nums:
            ans.append(int(product/num))
        return ans
