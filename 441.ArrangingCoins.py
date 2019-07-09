class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
#根据等差数列求和公式，a1*n+(n(n-1)d)/2,d=1,a1=1,得n+n(n-1)/2<=x(即argument里的n)
#换下公式x为项数，2x+x(x-1)<=2n,求x。x<=sqrt(2n+1/4)-1/2,因此求后边部分，然后对其取整，因为x必为整数。
        return int(math.sqrt(2n+0.25)-0.5)


#一个蠢爆了的做法。。。哭
#        if n==0:
#        	return 0
#        elif n==1:
#        	return 1
#        else:
#        	i=1
#        	while True:
#        		if n>=0:
#        			n=n-i
#        			i+=1
#        		else:
#        			break
#        	return i-1

