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