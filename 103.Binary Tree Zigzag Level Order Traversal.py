# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        depth = 0
        queue = [[root]]
        ans = []
        while queue:
            temp = []
            visited = []
            nodes = queue.pop(0)
            for node in nodes:
                visited.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                queue.append(temp)
            if not depth % 2:
                ans.append(visited)
            else:
                ans.append(visited[::-1])
            depth += 1
        return ans