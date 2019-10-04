class BinaryTree():

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solutions(object):

	def inorderTraverse(self, root, result):
		if root == None:
			return None
		self.inorderTraverse(root.left, result)
		result.append(root.val)
		self.inorderTraverse(root.right, result)

	def preorderTraverse(self, root, result):
		if root == None:
			return None
		result.append(root.val)
		self.preorderTraverse(root.left, result)
		self.preorderTraverse(root.right, result)

	def postorderTraverse(self, root, result):
		if root == None:
			return None
		self.postorderTraverse(root.left, result)
		self.postorderTraverse(root.right, result)
		result.append(root.val)

	# Recursion
	def traverse(self, root, method = 'preorder'):
		result = []
		if method == 'preorder':
			self.preorderTraverse(root, result)
		elif method == 'inorder':
			self.inorderTraverse(root, result)
		elif method == 'postorder':
			self.postorderTraverse(root, result)
		return result

	# Dive & Conquer
	def preorderTraverse_DC(self, root):
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
print(y.traverse(x, 'postorder'))