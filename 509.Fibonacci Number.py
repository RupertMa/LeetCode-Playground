class Solution:
    def __init__(self):
        self.nums = {0:0,1:1}
        
    def fib(self, N: int) -> int:
        if N in self.nums:
            return self.nums[N]
        
        n = 2
        while n <= N:
            self.nums[n] = self.nums[n-1] + self.nums[n-2]
            n += 1
        return self.nums[N]