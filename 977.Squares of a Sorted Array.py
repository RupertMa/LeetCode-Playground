class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return list(map(lambda x:x**2,sorted(A, key = lambda x:abs(x-0))))