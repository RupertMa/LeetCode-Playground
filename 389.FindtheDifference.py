class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        l=[]
        for i in range(len(s)):
            if s[i]==t[i]:continue
            else:
                l.append(t[i])
                del t[i]
        if len(s)!=len(t):
            for i in range(len(s),len(t)):
                l.append(t[i])
        return ''.join(l)

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ds = collections.Counter(s)
        dt = collections.Counter(t)
        return (dt - ds).keys().pop()