class Solution:
    # Time complexity: Nlog(K)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        ans = []
        for i in range(K):
            heapq.heappush(ans, (-self.Eucli(points[i]), points[i]))
        for i in range(K,len(points)):
            dist = self.Eucli(points[i])
            if -dist > ans[0][0]:
                _ = heapq.heappop(ans)
                heapq.heappush(ans, (-dist, points[i]))
        return [i[1] for i in ans]


    def Eucli(self, v):
        return (v[0]**2 + v[1]**2)


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        dist = lambda x,y: ((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5
        for point in points:
            heapq.heappush(heap, (dist(point, [0,0]), point))
        ans = [heapq.heappop(heap)[1] for i in range(k)]
        return ans
        # Time complexity: O(NlogN)
        # Space complexity: O(N)
