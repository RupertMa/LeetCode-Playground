# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        result = self.preorderTraverse(root)
        if len(result) >= 2:
            return sorted(list(result))[1]
        return -1
    
    def traverse(self, root, result):
        if not root:
            return None
        result.add(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)
    
    def preorderTraverse(self, root):
        result = set()
        self.traverse(root, result)
        return result