class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)-1
        for j in s:
            ans += (ord(j)-64) * 26**n
            n -= 1
        return ans
            