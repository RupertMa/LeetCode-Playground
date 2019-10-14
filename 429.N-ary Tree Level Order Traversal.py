"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = [[root]]
        ans = []
        while queue:
            temp = []
            children = []
            curNodes = queue.pop(0)
            for node in curNodes:
                if node:
                    temp.append(node.val)
                    if node.children:
                        children.extend(node.children)
            if children:
                queue.append(children)                        
            if temp:
                ans.append(temp)
        return ans