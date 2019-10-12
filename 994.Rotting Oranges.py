class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = set()
        ans = -1
        rotten= set()
        pos = list(zip([1,0,0,-1],[0,1,-1,0]))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    rotten.add((i,j))
        rotten = [rotten]
        while rotten:
        	cells = rotten.pop(0)
        	temp = set()
        	for c in cells:
        		for p in pos:
        			if (c[0]+p[0] >=0) and (c[0]+p[0] < n) and (c[1]+p[1]>=0) and (c[1]+p[1]<m) and ((c[0]+p[0],c[1]+p[1]) in fresh):
        				fresh.remove((c[0]+p[0],c[1]+p[1]))
        				temp.add((c[0]+p[0],c[1]+p[1]))
        	if temp:
        		rotten.append(temp)
        	ans += 1
        if fresh:
            return -1
        return ans