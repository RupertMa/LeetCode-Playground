# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        from collections import deque
        self.stack = deque([])
        self.helper(root)

    def helper(self, root):
        if root.left:
            self.helper(root.left)
        self.stack.append(root)
        if root.right:
            self.helper(root.right)

    def next(self) -> int:
        cur = self.stack.popleft()
        return cur.val

    def hasNext(self) -> bool:
        return self.stack



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
