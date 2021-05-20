# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #method1 dfs
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        ans = 0
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if node.val >= L and node.val <= R:
                ans += node.val
        return ans

    # method2 inorder traverse w/ resursion
    def __init__(self):
        self.ans = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.traverse(root, low, high)
        return self.ans

    def traverse(self, root, low, high):
        if not root:
            return None
        if root.left:
            self.traverse(root.left, low, high)
        if low <= root.val <= high:
            self.ans += root.val
        if root.right:
            self.traverse(root.right, low, high)

    # method3 inorder traverse w/ iteration
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop()
            else:
                break
            if low <= root.val <= high:
                ans += root.val
            root = root.right
        return ans

    # method4 utilize the property of BST
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0
        stack = []
        while True:
            while root:
                stack.append(root)
                if root.val >= low:
                    root = root.left
                else:
                    break
            if stack:
                root = stack.pop()
            else:
                break
            if low <= root.val <= high:
                ans += root.val
            root = None if root.val >= high else root.right
        return ans
