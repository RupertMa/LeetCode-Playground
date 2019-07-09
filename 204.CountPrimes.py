class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        isPrime=[True]*max(n,2)
        isPrime[0]=isPrime[1]=False
        for i in range(int(math.sqrt(n))+1):
        	if isPrime[i]:
        		p=i*2
        		while p<n:
        			isPrime[p]=False
        			p+=i
        return sum(isPrime)
#埃拉托斯特尼筛法求质数
#标记用列表构造





#        count=c2=0
#        for i in range(n-1):
#        	i=i+1
#        	for a in range(i):
#        		a=a+1
#        		if i%a==0:
#        			count+=1
#        	if count==2: c2+=1
#        	count=0
#        return c2