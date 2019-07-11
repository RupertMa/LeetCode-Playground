class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if not n:
            return None
        m = len(board[0])
        
        visited = [[False] * m for i in range(n)] 
        
        for i in range(n):
            for j in range(m):
                if (board[i][j] == 'O') & (not visited[i][j]):
                    region = self.bfs(i,j,m,n,visited,board)
                    for p in region:
                        board[p[0]][p[1]] = 'X'

                    
    def isValid(self, point, m, n):
        return point[0]>=0 and point[0]<n and point[1]>=0 and point[1]<m
        
    def bfs(self, i, j, m, n, visited, board):
        neighbor = list(zip([1,0,-1,0],[0,1,0,-1]))
        queue = [(i,j)]
        visited[i][j] = True
        region = []
        trigger = False
        while queue:
            front = queue.pop(0)
            if front[0]==0 or front[0]==n-1 or front[1]==0 or front[1]==m-1:
                trigger = True
            region.append(front)
            for p in neighbor:
                point = (front[0]+p[0], front[1]+p[1])
                #print(self.isValid(point,m,n))
                if self.isValid(point,m,n):
                    if (board[point[0]][point[1]]=='O') & (not visited[point[0]][point[1]]):
                        queue.append(point)
                        visited[point[0]][point[1]] = True
        if trigger: return [] 
        return region
                    