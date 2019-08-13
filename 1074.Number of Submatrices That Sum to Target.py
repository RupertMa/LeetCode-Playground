class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        preSumMatrix = [[0] * (m+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                preSumMatrix[i][j] = preSumMatrix[i][j-1] + preSumMatrix[i-1][j] + matrix[i-1][j-1] - preSumMatrix[i-1][j-1]

        ans = set()
        for lx in range(n):
            for rx in range(lx+1,n+1):
                temp = {0:[-1]}
                for j in range(1,m+1):
                    diff = preSumMatrix[rx][j] - preSumMatrix[lx][j]
                    if diff - target in temp:
                        for h in temp[diff-target]:
                            ans.add((lx+1,h+1,rx,j))
                    temp[diff] = temp.get(diff,[]) + [j]

        return len(ans)
