class KthLargest:
    import heapq

    # Time complexity: klog(k)
    def __init__(self, k: int, nums: List[int]):
        self.ans = []
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for i in range(min(k, len(nums))):
            self.ans.append(-1 * heapq.heappop(nums))
        heapq.heapify(self.ans)
        self.Min = float('-inf') if k > len(self.ans) else heapq.heappop(self.ans)

    # Time complexity: log(k)
    def add(self, val: int) -> int:
        if val > self.Min:
            heapq.heappush(self.ans, val)
            self.Min =  heapq.heappop(self.ans)
        return  self.Min

class KthLargest:
    # Time complexity: klog(k)
    def __init__(self, k: int, nums: List[int]):
        if len(nums) >= k:
            self.elements = sorted(nums)[-k:]
            self.ans = self.elements.pop(0)
        else:
            self.elements = sorted(nums)
            self.ans = float('-inf')

    # Time complexity: klog(k)
    def add(self, val: int) -> int:
        if val > self.ans:
            self.elements.append(val)
            self.elements = sorted(self.elements)
            self.ans = self.elements.pop(0)

        return self.ans


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
