class Solution:
    def minOperations(self, s: str) -> int:
        size = len(s)
        start_one = 0
        # starting with 1
        for i, j in enumerate(s):
            if (i % 2 and  j != '0') or ((not i % 2) and j != '1'):
                start_one += 1
        return min(start_one, size - start_one)
        # Time complexity: O(N)
