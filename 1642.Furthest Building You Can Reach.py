from typing import List
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        prev = heights[0]
        jump = 0
        heap = [0] * ladders if ladders else None
        heap_sum = 0
        for i, height in enumerate(heights[1:]):
            diff = height - prev
            if diff > 0:
                if heap and diff > heap[0]:
                    _ = heapq.heappop(heap)
                    heap_sum -= _
                    heapq.heappush(heap, diff)
                    heap_sum += diff
                jump += diff
            if jump - heap_sum > bricks:
                return i
            prev = height
        return i+1

        # Space complexity: O(N)
        # Time complexity: O(NlogN)
