# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        top=1
        btm=n
        while top<=btm:
        	mid=(top+btm)/2
        	if isBadVersion(mid): #True
        		btm=mid-1
        	else:
        		top=mid+1
        return top
#此乃真的二分法。。。我自己写的下面那个的效率是个啥。。。


#        a=1
#        b=n
#        while b-a!=1:
#        	mid=(a+b)/2
#        	if isBadVersion(mid): #True
#        		b=mid
#        	else:
#        		a=mid
#        if isBadVersion(a):
#        	return a
#        else:
#        	return b


