class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# Method 2
class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = [0]
        Sum = 0
        for i in nums:
            Sum += i
            self.preSum.append(Sum)
            
        

    def sumRange(self, i: int, j: int) -> int:
        return self.preSum[j+1] - self.preSum[i]