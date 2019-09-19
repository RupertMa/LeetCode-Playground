# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root,1)]
        while queue:
            (curNode, depth) = queue.pop(0)
            if (not curNode.left) and (not curNode.right):
                return depth
            if curNode.left:
                queue.append((curNode.left, depth+1))
            if curNode.right:
                queue.append((curNode.right, depth+1))
        return depth