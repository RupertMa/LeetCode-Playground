class Solution:
    def isValid(self, point,m,n):
            return point[0] < m and point[0] >= 0 and point[1] < n and point[1] >= 0
    
    def bfs(self, grid, visited, x, y, m, n):
        neighbor = list(zip([1,0,-1,0],[0,1,0,-1]))
        queue = [(x,y)]
        visited[x][y] = True
        while queue:
            front = queue.pop(0)
            for p in neighbor:
                point = (p[0] + front[0], p[1] + front[1])
                if self.isValid(point,m,n) and grid[point[0]][point[1]] =='1' and (not visited[point[0]][point[1]]):
                    visited[point[0]][point[1]] = True
                    queue.append(point)
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) 
        if m == 0:
            return 0        
        n = len(grid[0])

        visited = [[False] * n for i in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (not visited[i][j]):
                    #print(i,j)
                    ans += 1
                    self.bfs(grid, visited, i, j, m, n)
        return ans
            