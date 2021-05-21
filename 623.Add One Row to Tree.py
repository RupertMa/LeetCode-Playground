# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        from collections import deque
        cur_depth = 1
        queue = deque([(root, cur_depth)])
        while queue:
            (node, cur_depth) = queue.popleft()
            if cur_depth == depth - 1:
                cur = node.left
                node.left = TreeNode(val)
                node.left.left = cur
                cur = node.right
                node.right = TreeNode(val)
                node.right.right = cur
            else:
                if node.left:
                    queue.append((node.left, cur_depth+1))
                if node.right:
                    queue.append((node.right, cur_depth+1))
            if cur_depth > depth -1:
                break
        return root
