class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        n = len(grid)
        if not n:
            return 0
        m = len(grid[0])
        left = [[0] * m for i in range(n)]
        right = [[0] * m for i in range(n)]
        up = [[0] * m for i in range(n)]
        down = [[0] * m for i in range(n)]
        
        for i in range(n):
            kill = 0
            for j in range(m):
                if grid[i][j] =='E':
                    kill += 1
                elif grid[i][j] == 'W':
                    kill = 0
                    left[i][j] = kill
                else:
                    left[i][j] = kill
        for i in range(n):
            kill = 0
            for j in range(m-1,-1,-1):
                if grid[i][j] =='E':
                    kill += 1
                elif grid[i][j] == 'W':
                    kill = 0
                    right[i][j] = kill
                else:
                    right[i][j] = kill
        for j in range(m):
            kill = 0
            for i in range(n):
                if grid[i][j] == 'E':
                    kill += 1
                elif grid[i][j] == 'W':
                    kill = 0
                    up[i][j] = kill
                else:
                    up[i][j] = kill
        for j in range(m):
            kill = 0
            for i in range(n-1,-1,-1):
                if grid[i][j] == 'E':
                    kill += 1
                elif grid[i][j] == 'W':
                    kill = 0
                    down[i][j] = kill
                else:
                    down[i][j] = kill
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, sum([left[i][j], right[i][j], up[i][j], down[i][j], -3 if grid[i][j]=='E'else 0]))
        return ans