class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0:
            if 3**round(math.log(n,3))==n:
                return True
            else:
                return False
        else:
            return False

        #log(243,3)=4.99999 非常奇怪，因此用round()，这是何道理呢？