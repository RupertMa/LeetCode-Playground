# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        import sys
        self.lastVal = sys.maxsize * -1 
        
    def isValidBST(self, root: TreeNode) -> bool:
        # Traverse
        if not root:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.lastVal >= root.val:
            return False
        self.lastVal = root.val
        if not self.isValidBST(root.right):
            return False
        return True

    # Dive and Conquer:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.divConq(root, sys.maxsize *-1, sys.maxsize)

    def divConq(self, root, minVal, maxVal):
        
        if root==None:
            return True
        
        if (root.val <= minVal)  | (root.val >= maxVal):
            return False

        return self.divConq(root.left, minVal,min(maxVal,root.val))  & self.divConq(root.right, max(minVal, root.val), maxVal)

        