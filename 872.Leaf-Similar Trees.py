# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = self.getLeaf(root1)
        leaves2 = self.getLeaf(root2)
        return leaves1 == leaves2
    
    
    def getLeaf(self, root):
        leaves = []
        stack = [root]
        while stack:
            curNode = stack.pop()
            if curNode.left:
                stack.append(curNode.left)
            if curNode.right:
                stack.append(curNode.right)
            if (not curNode.left) and (not curNode.right):
                leaves.append(curNode.val)
        return leaves
                