class Solution:
    def findMin(self, nums: List[int]) -> int:
        lastElement = nums[-1]
        l = 0
        r = len(nums) - 1
        while l <= r:
            median = (l + r) // 2
            if nums[median] > lastElement:
                l = median + 1
            else:
                r = median - 1
        return nums[l]