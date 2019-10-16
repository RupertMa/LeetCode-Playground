"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            curNode = stack.pop()
            if curNode.children:
                stack.extend(curNode.children[::-1])
            ans.append(curNode.val)
        return ans
            