class Solution:
    def sumBase(self, n: int, k: int) -> int:
        lst=''
        while n:
        	rmd=n%k
        	n=n//k
        	lst=lst+str(rmd)
        return sum([int(i) for i in lst[::-1]])
        # Time complexity: O(N)
        # Space complexity: O(N)
