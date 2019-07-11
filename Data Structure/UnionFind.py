class UnionFind(object):
	def __init__(self, hashMap):
		self.unionFind = hashMap

	def __repr__(self):
		return str(self.unionFind)

	def find(self, x):
		parent = x
		while self.unionFind[parent]!=parent:
			parent = self.unionFind[parent]
		return parent

	def union(self, x, y):
		parentX = self.find(x)
		parentY = self.find(y)
		if parentX != parentY:
			self.unionFind[parentX] = parentY

	def compressedFind(self, x):
		parent = self.unionFind[x]
		while parent != self.unionFind[parent]:
			parent = self.unionFind[parent]

		while parent != self.unionFind[x]:
			Next = self.unionFind[x]
			self.unionFind[x] = parent
			x = Next

		return parent