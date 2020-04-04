# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.Set = set()
        self.root = self.rectify(root)
        
        
    
    def rectify(self,root):
        root.val = 0
        queue = [root]
        while queue:
            curNode = queue.pop(0)
            if curNode:
                self.Set.add(curNode.val)
                if curNode.left:
                    curNode.left.val = curNode.val * 2 + 1
                    queue.append(curNode.left)
                if curNode.right:
                    curNode.right.val = curNode.val * 2 + 2
                    queue.append(curNode.right) 
        return root

    def find(self, target: int) -> bool:
        return target in self.Set

                
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)