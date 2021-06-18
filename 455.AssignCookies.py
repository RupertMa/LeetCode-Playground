class Solution(object):
	def findContentChildren(g,s):
		g.sort(reverse=True)
		s.sort(reverse=True)
		#print g,s
		res=0
		i,j=0,0
		while j<len(s) and i<len(g):
			if s[j]>=g[i]:
				res+=1
				j+=1
				i+=1
			else:
				i+=1
		return res

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        from collections import deque
        g = deque(sorted(g))
        s = deque(sorted(s))
        count = 0
        while g and s:
            if g[0] <= s[0]:
                count += 1
                g.popleft()
            s.popleft()
        return count
  #Time complexity: O(nlogn)
