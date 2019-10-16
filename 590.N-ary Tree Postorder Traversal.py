"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.ans = []

    def postorder(self, root):
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root:
            return None

        if not root.children:
            self.ans.append(root.val)
            return None

        for child in root.children:
            self.helper(child)
        self.ans.append(root.val)