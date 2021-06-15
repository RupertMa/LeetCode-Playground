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

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        from collections import defaultdict
        positions = defaultdict(list)
        for i,j in enumerate(t):
            positions[j].append(i)
        prev = -1
        for c in s:
            if positions[c]:
                cond = True
                for p in positions[c]:
                    if p > prev:
                        cond = False
                        prev = p
                        break
                if cond:
                    return False
            else:
                return False
        return True
