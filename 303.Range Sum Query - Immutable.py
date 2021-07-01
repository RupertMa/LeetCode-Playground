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

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prev_l = 0
        self.prev_r = len(self.nums) - 1
        self.sum = sum(nums)


    def sumRange(self, left: int, right: int) -> int:
        if left < self.prev_l:
            for i in range(left, self.prev_l):
                self.sum += self.nums[i]
        elif left > self.prev_l:
            for i in range(self.prev_l, left):
                self.sum -= self.nums[i]
        if right < self.prev_r:
            for i in range(right+1, self.prev_r+1):
                self.sum -= self.nums[i]
        elif right > self.prev_r:
            for i in range(self.prev_r+1, right+1):
                self.sum += self.nums[i]
        self.prev_l = left
        self.prev_r = right
        return self.sum

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
