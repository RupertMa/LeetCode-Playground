# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        stack = [root] if root else []
        while stack:
            cur = stack.pop()
            nodes.append(cur)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        nodes = sorted(nodes, key=lambda x:x.val)
        return self.buildBST(nodes)
        # Time complexity: O(NlogN)
        # Space complexity: O(N)

    def buildBST(self, nodes):
        if not nodes:
            return None
        mid = len(nodes)//2
        node = nodes[mid]
        node.left = self.buildBST(nodes[:mid])
        node.right = self.buildBST(nodes[mid+1:])
        return node
