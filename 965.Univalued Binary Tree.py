# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        queue = [root]
        while queue:
            cur = queue.pop(0)
            if cur.val != val:
                return False
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return True
        