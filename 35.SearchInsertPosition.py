class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        c=1
        if target in nums:
        	return nums.index(target)
        else:
        	for i in nums:
        		if target<i:
        			return nums.index(i)
        		else:
        			c=0
        	if c==0:
        		return len(nums)
