# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        idx = self.argmax(nums)
        root = TreeNode(nums[idx])
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root

    

    def argmax(self, lst):
        temp = lst[0]
        ans = 0
        for i,j in enumerate(lst):
            if j > temp:
                temp = j
                ans = i
        return ans