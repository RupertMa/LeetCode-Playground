class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or str(x) != str(x)[::-1]:
            return False
        return True
