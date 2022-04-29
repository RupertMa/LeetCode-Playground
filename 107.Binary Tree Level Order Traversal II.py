# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        stack = [[root]] if root else root
        while stack:
            curList = stack.pop(0)
            temp = []
            temp_ans = []
            for node in curList:
                temp_ans.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                stack.append(temp)
            if temp_ans:
                ans = [temp_ans] + ans
        return ans
