class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
        	newnums=nums[nums.index(i)+1:]
        	for s in newnums:
        	    if i+s==target:
        			return [nums.index(i),newnums.index(s)+nums.index(i)+1]
#自己改出来了！没看参考答案！开心！

#算法效率又不够嘤嘤嘤        
#        c1=c2=0
#        for i in nums:
#        	for s in nums[c1+1:]:
#        		c2+=1
#        		if i+s==target:
#        			return [c1,c2]
#        	c2=c1+1
#        	c1+=1