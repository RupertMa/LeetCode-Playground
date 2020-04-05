# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        self.height = self.getDepth(root)
        self.width = 2**self.height - 1
        self.treeString = [[""] * self.width for i in range(self.height)]
        self.traverse(root, 1, self.width >> 1)  # self.width // 2**1
        return self.treeString
    
    
    def getDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
    
    def traverse(self, root, depth, offset):
        if not root: return
        self.treeString[depth - 1][offset] = str(root.val)
        gap = 1 + self.width >> depth + 1  # (1 + self.width) // 2**(depth + 1)
        self.traverse(root.left, depth + 1, offset - gap)
        self.traverse(root.right, depth + 1, offset + gap)
