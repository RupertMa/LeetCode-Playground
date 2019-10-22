# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
    	self.helper(root)
    	return root


    def helper(self, root):
    	if not root:
    		return 0

    	if (not root.left) and (not root.right):
    		if root.val == 0:
    			return 0
    		else:
    			return 1

    	left = self.helper(root.left) 
    	right = self.helper(root.right)

    	if left+right+root.val == 0:
    		root = None
    		return 0

    	if left == 0:
    		root.left = None
    	if right == 0:
    		root.right = None

    	return left+right+root.val