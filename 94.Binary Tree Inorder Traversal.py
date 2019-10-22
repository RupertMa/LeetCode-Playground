# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if root and (not root.left) and (not root.right):
            return [root.val]

        ans = [root.val]
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + ans + right