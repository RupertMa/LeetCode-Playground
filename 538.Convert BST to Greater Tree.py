# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.cum = 0

#A more concise and elegant method:
    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root


# with helper method. 
    # def convertBST(self, root: TreeNode) -> TreeNode:
    #     self.helper(root)
    #     return root

    # def helper(self, root):
    #     if not root:
    #         return None

    #     if (not root.left) and (not root.right):
    #         self.cum += root.val
    #         root.val = self.cum
    #         return None

    #     self.helper(root.right)
    #     self.cum += root.val
    #     root.val = self.cum
    #     self.helper(root.left)

    #     return None


