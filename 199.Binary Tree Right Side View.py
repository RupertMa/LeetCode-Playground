# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        queue = [[root]]
        ans = []
        while queue:
            temp = []
            curNodes = queue.pop(0)
            for node in curNodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            ans.append(node.val)
            if temp:
                queue.append(temp)
        return ans


    #Improvement: Simplify data structure of queue. Use queue length and pop to get each level of a tree.
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        queue = [root]
        ans = []
        while queue:
            size = len(queue)
            for i in range(size):
                top = queue.pop(0)
                if i == 0:
                    ans.append(top.val)
                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
        return ans

    #Approach 3: Use two counters to count the num of nodes in next level and the num of nodes left in current level.
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        queue = [root]
        ans = []
        num = 1 ; next = 0
        while queue:
            p = queue.pop(0)
            if p.left:
                queue.append(p.left)
                next += 1
            if p.right:
                queue.append(p.right)
                next += 1
            num -= 1
            if num ==0:
                ans.append(p.val)
                num = next
                next = 0
        return ans

# 2025/03/02
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                queue = next_level
            else:
                queue = []
            ans.append(node.val)
        return ans
