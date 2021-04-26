class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-i-1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-i-1][i]
                matrix[n-i-1][j] = matrix[n-j-1][n-i-1]
                matrix[n-j-1][n-i-1] = matrix[i][n-j-1]
                matrix[i][n-j-1] = temp

x = Solution()
print(x.rotate([[1,2,3],[4,5,6],[7,8,9]]))
