# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        ans = []
        while queue:
            ans.append(sum([node.val for node in queue])/len(queue))
            nqueue = []
            for node in queue:
                if node.left:
                    nqueue.append(node.left)
                if node.right:
                    nqueue.append(node.right)
            queue = nqueue
        return ans