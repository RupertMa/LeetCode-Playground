class BinaryTree():

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solutions(object):

	def traverse(self, root, result):
		if root == None:
			return None
		result.append(root.val)
		self.traverse(root.left, result)
		self.traverse(root.right, result)

	# Recursion
	def preorderTraverse(self, root):
		result = []
		self.traverse(root, result)
		return result

	# Dive & Conquer
	def preorderTraverse(self, root):
		result = []

		if root == None:
			return None
		result.append(root.val)

		left = self.preorderTraverse(root.left)
		right = self.preorderTraverse(root.right)

		if left:
			result.extend(left)
		if right:
			result.extend(right)

		return result


x = BinaryTree(1)
x.left = BinaryTree(2)
x.right = BinaryTree(3)
x.left.left = BinaryTree(4)
x.left.right = BinaryTree(5)


y = Solutions()
print(y.preorderTraverse(x))