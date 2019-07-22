from heapq import *
class MedianFinder:
    
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        heappush(self.minHeap,num)
        minTop = self.minHeap[0] if len(self.minHeap) else None
        maxTop = -1 * self.maxHeap[0] if len(self.maxHeap) else minTop-1
        if  len(self.minHeap) - len(self.maxHeap) > 1 or minTop < maxTop:
            heappush(self.maxHeap, heappop(self.minHeap) * -1)
        if len(self.maxHeap) - len(self.minHeap) > 1 :
            heappush(self.minHeap, heappop(self.maxHeap) * -1)

        
        
    def findMedian(self) -> float:
        right = len(self.minHeap)
        left = len(self.maxHeap)
        if ( right + left ) % 2:
            return self.minHeap[0] if right>left else self.maxHeap[0] * -1
        else:
            return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()