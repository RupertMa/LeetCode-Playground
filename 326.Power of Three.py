class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return self.helper(n)

    def helper(self, n):
        if n!= int(n) or n < 3:
            return False
        elif n==3:
            return True
        else:
            return self.helper(n/3)
