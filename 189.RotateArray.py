class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ln=len(nums)
        k=k%ln
        nums[:]=nums+nums[:ln-k]
    	del nums[0:ln-k]


#menthod 2自己输入[1,2],k=1通过了测试但是leetcode的output和自己的不一样，怎么都不pass。What's wrong？
#后来发现了原因nums后面要加[:]        
#        ln=len(nums)
#        k=k%ln
#        lastnum=nums[0:ln-k]
#        nums[:]=nums[ln-k:]
#        nums[:]=nums+lastnum


#method 1:
#        ln=len(nums)
#         k=k%ln
#        for i in range(ln-k):
#            nums.append(nums[i])
#        del nums[0:ln-k]