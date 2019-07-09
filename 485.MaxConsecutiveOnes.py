class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=b=0
        for i in nums:
        	if i==0:
        		a=0
        	if i==1:
        		a+=1
        		b=max(a,b)
        return b