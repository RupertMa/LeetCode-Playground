# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.val == subRoot.val:
                if self.isEqual(cur, subRoot):
                    return True
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False

    def isEqual(self, root1, root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (not root2 and root1):
            return False
        if root1.val != root2.val:
            return False
        left = self.isEqual(root1.left, root2.left)
        right = self.isEqual(root1.right, root2.right)
        return left and right

    # Time Complexity: O(MN)
    # Space Complexity: O(N)
