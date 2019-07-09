class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        for x in [2,3,5]:
        	while num%x==0:
        		num/=x
        return num==1

#这个方法实在有些精妙。首先是for和while的结合使用。先不断对num除2，再除3和5。
#得到最后的num值后再判断是否等于1。第一个条件语句是为了提高算法效率，把小于0的部分
#摘出去。



#又一次算法效率太低。。。哭        
#        while True:
#        	if num%2==0:
#        		num=num/2
#        	elif num%3==0:
#        		num=num/3
#        	elif num%5==0:
#        		num=num/5
#        	elif num==1:
#        		return True
#        	else:
#        		return False
#        		break
