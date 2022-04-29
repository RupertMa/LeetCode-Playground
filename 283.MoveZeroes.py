from typing import List

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        y = 0 #position of the 1st zero after current position or the current position itself
        for x in range(len(nums)):
            if nums[x]:
                nums[x], nums[y] = nums[y], nums[x]
                y += 1
        
        #算法具体怎么实现还是不太清楚
        #这个叫冒泡法排序?
        # Time complexity: O(N)
        # Space complexity: O(1)

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l):
            if nums[i]== 0:
                j = i+1
                while j < l and nums[j] == 0:
                    j += 1
                if j < l:
                    nums[i], nums[j] = nums[j], nums[i]
        # Time complexity: O(N)
        # Space complexity: O(1)

nums = [0,1,0,3,12,0,0]
x = Solution()
x.moveZeroes(nums)
print(nums)
