# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        bfs_queue = [(root,1)]
        while bfs_queue:
            currentNode,leaf = bfs_queue.pop(0)
            if currentNode:
                if currentNode.left:
                    bfs_queue.append((currentNode.left,0))
                if currentNode.right:
                    bfs_queue.append((currentNode.right,1))
                if (not currentNode.left) and (not currentNode.right) and leaf==0:
                    ans += currentNode.val
        return ans
