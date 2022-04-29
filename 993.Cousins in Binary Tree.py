# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [[(root, 1, None)]]
        x_depth = y_depth = 0
        x_parent = y_parent = None
        while queue:
            temp = []
            curNodes = queue.pop(0)
            for curNode, depth, parent in curNodes:
                if curNode.val == x:
                    x_depth = depth
                    x_parent = parent
                elif curNode.val ==y:
                    y_depth = depth
                    y_parent = parent
                if curNode.left:
                    temp.append((curNode.left, depth+1, curNode.val))
                if curNode.right:
                    temp.append((curNode.right, depth+1, curNode.val))
            if x_depth or y_depth:
                return (x_depth==y_depth) and (x_parent!=y_parent)

            if temp:
                queue.append(temp)

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        par1, depth1 = self.traverse(root, 0, x)
        par2, depth2 = self.traverse(root, 0, y)
        return (par1!=par2) and (depth1==depth2)

    def traverse(self, root, depth, val):
        if root.val == val:
            return (None, depth)
        if (root.left and root.left.val == val) or (root.right and root.right.val == val):
            return (root, depth+1)
        left = self.traverse(root.left, depth+1, val) if root.left else (None, depth)
        right = self.traverse(root.right, depth+1, val) if root.right else (None, depth)
        return left if left[0] else right
