# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [[root]]     
        while queue:
            ans = []
            temp = []
            curNodes = queue.pop(0)
            for node in curNodes:
                if (not node):
                    ans.append(None)
                else:
                    ans.append(node.val)
                    temp.append(node.left)
                    temp.append(node.right)
            if ans != ans[::-1]:
                return False
            if temp:
                queue.append(temp)
        return True
                