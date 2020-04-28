class Solution:
    # Time complexity: nlogn
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        queue = [1]
        q_set = {1}
        factor = [2,3,5]
        for i in range(n):
            Min = heapq.heappop(queue)
            for f in factor:
                if Min * f not in q_set:
                    heapq.heappush(queue, Min*f)
                    q_set.add(Min*f)
        return Min