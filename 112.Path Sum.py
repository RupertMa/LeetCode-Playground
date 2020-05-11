# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return None
        queue = [root]
        pathSum = {root:root.val}
        while queue:
            curNode = queue.pop(0)
            if curNode.left:
                pathSum[curNode.left] = pathSum[curNode] + curNode.left.val
                queue.append(curNode.left)
            if curNode.right:
                queue.append(curNode.right)
                pathSum[curNode.right] = pathSum[curNode] + curNode.right.val
            if not curNode.left and not curNode.right and pathSum[curNode] == sum:
                return True
        return False