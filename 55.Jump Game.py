class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        zeros = []
        for i, num in enumerate(nums[:-1]):
            if num == 0:
                zeros.append(i)
        for zero in zeros:
            cond = True
            for i in range(zero-1, -1, -1):
                if zero - i < nums[i]:
                    cond = False
                    break
            if cond:
                return False
        return True
      # Time complexity: O(MN) N = len(nums) M = num of zeros
