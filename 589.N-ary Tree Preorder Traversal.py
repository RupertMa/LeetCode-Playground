"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        stack = [root] if root else root
        while stack:
            cur = stack.pop()
            if cur.children:
                stack.extend(cur.children[::-1])
            ans.append(cur.val)
        return ans
