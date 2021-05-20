# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inverseTraverse(root)
        return self.ans[k-1]

    def inverseTraverse(self, root):
        if root.left:
            self.inverseTraverse(root.left)
        self.ans.append(root.val)
        if root.right:
            self.inverseTraverse(root.right)

    # Time complexity: O(N)
    # Space complexity: O(N)
