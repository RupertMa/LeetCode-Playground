class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        y=0
        for x in range(len(nums)):
        	if nums[x]:
        		nums[x],nums[y]=nums[y],nums[x]
        		y+=1
        #算法具体怎么实现还是不太清楚
#这个叫冒泡法排序