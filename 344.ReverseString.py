class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        s.reverse()
        s="".join(s)
        return s

        #更简单的方法
        #return ''.join(reversed(s))
        #用reversed()