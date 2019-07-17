class heap(object):
	def __init__(self):
		self.items = []

	def getLeftNodeIndex(self, parentIndex):
		return parentIndex * 2 + 1

	def getRightNodeIndex(self, parentIndex):
		return parentIndex * 2 + 2

	def getParentNodeIndex(self, childIndex):
		return (childIndex - 1) // 2

	def swap(self,index1,index2):
		self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

	def heapify(self,unheapifiedItems):
		for item in unheapifiedItems:
			self.heapPush(item)
		return self.items

	def heapPop(self):
		if len(self.items) == 0:
			raise IndexError
		item = self.items[0]
		self.items[0] = self.items.pop() # self.items[0] = self.items.pop()
		self.heapifyDown()
		return item

	def heapPush(self, item):
		self.items.append(item)
		self.heapifyUp()

	def heapifyDown(self):
		size = len(self.items)
		parentIndex = 0
		leftChildIndex = self.getLeftNodeIndex(parentIndex)
		rightChildIndex = self.getRightNodeIndex(parentIndex)
		while leftChildIndex < size:
			if rightChildIndex < size and self.items[rightChildIndex] < self.items[parentIndex] and self.items[rightChildIndex] < self.items[leftChildIndex]:
				self.swap(rightChildIndex, parentIndex)
				parentIndex = rightChildIndex
				leftChildIndex = self.getLeftNodeIndex(parentIndex)
				rightChildIndex = self.getLeftNodeIndex(parentIndex)
			elif self.items[leftChildIndex] < self.items[parentIndex]:
				self.swap(leftChildIndex, parentIndex)
				parentIndex = leftChildIndex
				leftChildIndex = self.getLeftNodeIndex(parentIndex)
				rightChildIndex = self.getRightNodeIndex(parentIndex)
			else:
				break

	def heapifyUp(self):
		size = len(self.items)
		childIndex = size - 1
		parentIndex = self.getParentNodeIndex(childIndex)
		while parentIndex >= 0 and self.items[parentIndex] > self.items[childIndex]:
			self.swap(parentIndex, childIndex)
			childIndex = parentIndex
			parentIndex = self.getParentNodeIndex(childIndex)


	def hasLeftNode(self, paretIndex):
		return self.getLeftNodeIndex() < len(self.items)

	def hasRightNode(self, paretIndex):
		return self.getRightNodeIndex() < len(self.items)

	def hasParentNode(self, childIndex):
		return self.getParentNodeIndex() >= 0

