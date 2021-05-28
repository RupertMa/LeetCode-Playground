# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.buildBST(nums)

    def buildBST(self, nodes):
        if not nodes:
            return None
        length = len(nodes)
        m = length // 2
        cur = TreeNode(nodes[m])
        cur.left = self.buildBST(nodes[:m])
        cur.right = self.buildBST(nodes[m+1:])
        return cur

        
