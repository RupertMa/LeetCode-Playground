from heapq import *
class MedianFinder:
    
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []
        self.median = None
        

    def addNum(self, num: int) -> None:
        if not self.median:
            self.median = num
            heappush(self.minHeap, num)
        elif num > self.median:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)
        
        if len(self.minHeap) - len(self.maxHeap) > 1:
            self.median = heappop(self.minHeap)
            heappush(self.maxHeap, -1 * self.median)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            self.median = -1 *heappop(self.maxHeap)
            heappush(self.minHeap, self.median)
    
    def removeNum(self,num):
        if num in self.minHeap:
            self.minHeap.remove(num)
            heapify(self.minHeap)
        else:
            self.maxHeap.remove(-num)
            heapify(self.maxHeap)

        if len(self.minHeap) - len(self.maxHeap) > 1:
            self.median = heappop(self.minHeap)
            heappush(self.maxHeap, -1 * self.median)
        if len(self.maxHeap) - len(self.minHeap) > 1:
            self.median = -1 *heappop(self.maxHeap)
            heappush(self.minHeap, self.median)
        
    def findMedian(self) -> float:
        right = len(self.minHeap)
        left = len(self.maxHeap)
        if ( right + left ) % 2:
            return self.minHeap[0] if right>left else self.maxHeap[0] * -1
        else:
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        x = MedianFinder()
        ans = []
        for i in range(len(nums)):
            if i < k:
                x.addNum(nums[i])
            else:
                ans.append(x.findMedian())
                x.removeNum(nums[i-k])
                x.addNum(nums[i])
        ans.append(x.findMedian())
        return ans
        