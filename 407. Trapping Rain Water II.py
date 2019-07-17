class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        from heapq import heappush
        from heapq import heappop
        
        m = len(heightMap) ; n = len(heightMap[0]) 
        visited = [[False] * n for i in range(m)]
        heap = []
        for i in range(n):
            heappush(heap, (heightMap[0][i], (0,i)))
            heappush(heap, (heightMap[m-1][i], (m-1,i)))
            visited[0][i] = True
            visited[-1][i] = True
        for i in range(m):
            if not visited[i][0]:
                heappush(heap,(heightMap[i][0], (i,0)))
                heappush(heap,(heightMap[i][n-1],(i,n-1)))
                visited[i][0] = True
                visited[i][-1] = True
        dim = list(zip([0,1,0,-1],[1,0,-1,0]))
        cum = 0
        while heap:
            (height,point) = heappop(heap)
            for move in dim:
                dx = point[0] + move[0]
                dy = point[1] + move[1]
                if dx>=0 and dx < m and dy>=0 and dy < n and (not visited[dx][dy]):
                    heappush(heap, (max(height,heightMap[dx][dy]),(dx,dy)))
                    visited[dx][dy] = True
                    cum += max(0, height - heightMap[dx][dy])
                    #break
        return cum