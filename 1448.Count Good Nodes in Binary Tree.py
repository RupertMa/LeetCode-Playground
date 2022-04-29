# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans  = 0

    def goodNodes(self, root: TreeNode) -> int:
        max_val = root.val
        self.dfs(root, max_val)
        return self.ans


    def dfs(self, root, max_val):
        if not root:
            return None
        if root.val >= max_val:
            self.ans += 1
        max_val = max(max_val, root.val)
        if root.left:
            self.dfs(root.left, max_val)
        if root.right:
            self.dfs(root.right, max_val)

        # Time complexity: O(N)
        # Space complexity: O(1)
