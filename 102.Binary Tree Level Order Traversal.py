# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
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
            ans.append(visited)
        return ans
        