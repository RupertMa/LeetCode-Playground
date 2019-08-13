# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
class Solution:
    
    def getMinimumDifference(self, root):
        vals = self.traverTree(root)
        vals = sorted(vals)
        ans = sys.maxsize
        for i in range(1,len(vals)):
            ans = min(ans, vals[i]-vals[i-1])
        return ans
        
    def traverTree(self,tree):
        vals = []
        queue = [tree]
        while queue:
            current = queue.pop(0)
            vals.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return vals
