# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inorderTraverse(root)
        re_node = TreeNode(None)
        curNode = re_node
        for val in self.ans:
            curNode.right = TreeNode(val)
            curNode = curNode.right
        return re_node.right

    
    def inorderTraverse(self, root):
        if not root:
            return None

        if root.left:
            self.inorderTraverse(root.left)

        self.ans.append(root.val)

        if root.right:
            self.inorderTraverse(root.right)