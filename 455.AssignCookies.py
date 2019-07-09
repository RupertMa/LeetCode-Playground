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


g=list(raw_input('Enter g:'))
s=list(raw_input('Enter s'))
y=findContentChildren(g,s)
print y


