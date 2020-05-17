# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Time complexity: O(N)
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [[root]]
        while queue:
            temp = []
            deepestNodes = []
            nodes = queue.pop(0)
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                if not node.left and not node.right:
                    deepestNodes.append(node.val)
            if temp:
                queue.append(temp)
        return sum(deepestNodes)
            