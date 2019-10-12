# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t):
        if not t:
            return ""       
        return self.helper(t)[1:-1]

    def helper(self, node):    
        if not node:
            return None
        if (not node.left) and (not node.right):
            return '('+ str(node.val) + ')'

        left = self.helper(node.left)

        right = self.helper(node.right)    

        if not left:
            return '('+ str(node.val) + '()' + right + ')'
        if not right:
            return  '('+ str(node.val) + left + ')'
        return '('+ str(node.val) + left + right + ')'