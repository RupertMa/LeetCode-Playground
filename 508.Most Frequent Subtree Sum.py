# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        from collections import defaultdict
        self.ans = defaultdict(int)

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.postOrderTraverse(root)
        most_frequent = max(self.ans.values())
        ans = []
        for key, val in self.ans.items():
            if val == most_frequent:
                ans.append(key)
        return ans

    def postOrderTraverse(self, root):
        if not root:
            return 0
        left = self.postOrderTraverse(root.left) if root.left else 0
        right = self.postOrderTraverse(root.right) if root.right else 0
        subtree_sum = root.val + left + right
        self.ans[subtree_sum] += 1
        return subtree_sum

    # Time Complexity: O(N)
    # Space Complexity: O(N)
