class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        queueS = list(s)
        for i in t:
        	if not queueS:
        		return True
        	elif i == queueS[0]:
        		queueS.pop(0)
        if not queueS:
            return True
        return False
