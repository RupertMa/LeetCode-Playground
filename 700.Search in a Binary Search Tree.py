# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            elif node.val < val:
                if (node.right):
                    stack.append(node.right)
            elif node.val > val:
                if (node.left):
                    stack.append(node.left)
        return None