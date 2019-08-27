class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 0
        r = len(s) - 1
        l_w = None
        r_w = None
        vowel = set(['a','e','i','o','u','A','E','I','O','U'])
        s = list(s)
        while l < r :
        	while l < r and (l_w==None):
        		if s[l] in vowel:
        			l_w = l
        		l += 1
        	while l <= r and (r_w==None):
        		if s[r] in vowel:
        			r_w = r
        		r -= 1
        	if l_w !=None and r_w:
        		s[l_w],s[r_w] = s[r_w],s[l_w]
        	l_w = None
        	r_w = None
        return "".join(s)