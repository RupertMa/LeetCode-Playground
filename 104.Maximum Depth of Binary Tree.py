# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.depth = 0
    
    def maxDepth(self, root: TreeNode) -> int:
        # Traverse
        
        
        def helper(root, curDepth):
            if not root:
                return None
            if curDepth > self.depth:
                self.depth = curDepth
            helper(root.left, curDepth+1)
            helper(root.right, curDepth+1)
        
        
        helper(root, 1)
        
        return self.depth
        
        # Divide and Conquer    
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left,right) + 1