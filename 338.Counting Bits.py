class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        a=0
        b=[]
        while a<=num:
        	b.append(bin(a).count('1'))
        	a+=1
        return b





num=3
ans = [0]
for x in range(1, num + 1):
	ans += ans[x >> 1] + (x & 1),
print ans