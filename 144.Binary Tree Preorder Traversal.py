# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            ans = []
            ans.append(root.val)
            if root.left:
                ans.extend(self.preorderTraversal(root.left))
            if root.right:
                ans.extend(self.preorderTraversal(root.right))
            return ans
        
