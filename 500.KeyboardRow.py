class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a='QWERTYUIOPqwertyuiop'
        b='ASDFGHJKLasdfghjkl'
        c='ZXCVBNMzxcvbnm'
        a=list(a)
        b=list(b)
        c=list(c)
        l=[]
        counta=countb=countc=0
        for word in words:
        	word=list(word)
        	for character in word:
        		if character in a:
        			counta+=1
        		if character in b:
        			countb+=1
        		if character in c:
        			countc+=1
        	if len(''.join(word))==counta or len(''.join(word))==countb or len(''.join(word))==countc:
        		l.append(''.join(word))
        	counta=countb=countc=0
        return l
        

