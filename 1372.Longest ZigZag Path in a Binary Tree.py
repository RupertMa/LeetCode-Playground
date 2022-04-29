# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def longestZigZag(self, root: TreeNode) -> int:
        self.find(root, 'l', 0)
        self.find(root, 'r', 0)
        return self.ans

    def find(self, root, direction, length):
        if length:
            self.ans = max(length, self.ans)
        if root.left:
            if direction == 'l':
                self.find(root.left, 'r', length+1)
            else:
                self.find(root.left, 'l', 0)
        if root.right:
            if direction == 'r':
                self.find(root.right, 'l', length+1)
            else:
                self.find(root.right, 'r', 0)

# Time complexity: O(N)
# Space complexity: O(1)
