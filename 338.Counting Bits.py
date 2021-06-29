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


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        ans = [0, 1]
        length = 2
        pointer = 0
        while length <= n:
            prev_len = len(ans)
            while pointer < prev_len and length <= n:
                ans.append(ans[pointer]+1)
                pointer += 1
                length += 1
            pointer = 0
        return ans
