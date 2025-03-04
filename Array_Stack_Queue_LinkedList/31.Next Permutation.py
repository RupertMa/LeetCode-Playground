from typing import *

# 2025/03/03
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        cond = False
        for i in range(length - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = nums[i - 1]
                pivot_idx = i - 1
                cond = True
                break

        if not cond:
            nums[::] = nums[::-1]
            return

        cond = False
        for i in range(pivot_idx + 1, length):
            if nums[i] <= pivot:
                nums[i - 1], nums[pivot_idx] = nums[pivot_idx], nums[i - 1]
                cond = True
                break

        if not cond:
            nums[-1], nums[pivot_idx] = nums[pivot_idx], nums[-1]
            nums[pivot_idx + 1:] = nums[pivot_idx + 1:][::-1]
        else:
            nums[pivot_idx + 1:] = nums[pivot_idx + 1:][::-1]