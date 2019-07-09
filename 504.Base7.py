class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        n=abs(num)
        while n:
        		rmd=n%7
        		n=n/7
        		lst.append(str(rmd))
        return ['','-'][num<0]+lst[::-1] or '0'


