# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Iteration
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        queue = [(p,q)]
        while queue:
            x, y = queue.pop(0)
            if not x or not y or x.val != y.val:
                return False
            if x.left or y.left:
                queue.append((x.left, y.left))
            if x.right or y.right:
                queue.append((x.right, y.right))
        return True

    # Recursion
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (not p and q) or (p and not q):
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) & self.isSameTree(p.right, q.right)