class Solution:
    def inQueue(self, num, deque):
        condition = num > deque[-1] if deque else False
        while condition:
            deque.pop()
            condition = num > deque[-1] if deque else False
        deque.append(num)
    
    def outQueue(self, num, deque):
        if num == deque[0]:
            deque.pop(0)
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if len(nums)==1 and k ==1:
            return nums
        ans = [ ]
        deque = [ ]
        for i in range(len(nums)):
            self.inQueue(nums[i], deque)
            if i-k >= 0 :
                self.outQueue(nums[i-k], deque)
            if i >= k -1:
                ans.append(deque[0])
                
        return ans