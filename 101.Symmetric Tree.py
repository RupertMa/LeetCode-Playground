# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [[root]]
        while queue:
            ans = []
            temp = []
            curNodes = queue.pop(0)
            for node in curNodes:
                if (not node):
                    ans.append(None)
                else:
                    ans.append(node.val)
                    temp.append(node.left)
                    temp.append(node.right)
            if ans != ans[::-1]:
                return False
            if temp:
                queue.append(temp)
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [[root]]
        while queue:
            temp = []
            nodes = queue.pop(0)
            for cur in nodes:
                if cur:
                    temp.append(cur.left)
                    temp.append(cur.right)
            c = [i.val if i else i for i in temp]
            if c[:len(c)//2] != c[len(c)//2:][::-1]:
                return False
            else:
                if temp:
                    queue.append(temp)
        return True

    # Time complexity: O(N)
    # Space complexity: O(N)
