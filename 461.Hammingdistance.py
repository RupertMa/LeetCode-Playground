class Solution(object):
	def hammingDistance(x, y):
		"""
		:type x: int
		:type y: int
		:rtype: int
		"""
		return bin(x ^ y).count('1')

	x=int(raw_input('Enter X:'))
	y=int(raw_input('Enter Y:'))
	z=hammingDistance(x,y)
	print z