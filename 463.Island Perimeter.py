class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        island = set()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    island.add((i,j))
        moves = list(zip([0,1,-1,0],[1,0,0,-1]))    
        Sum = 0
        for i in island:
            add = 4
            for mv in moves:
                if (i[0] + mv[0], i[1]+mv[1]) in island:
                    add -= 1
            Sum += add
        return Sum
        