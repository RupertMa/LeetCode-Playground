# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        
        if not root:
            return paths
        if (not root.left) and (not root.right):
            return [str(root.val)]
        
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        
        for path in leftPaths:
            paths.append(str(root.val)+'->'+str(path))
        for path in rightPaths:
            paths.append(str(root.val)+'->'+str(path))
        
        return paths