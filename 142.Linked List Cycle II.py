# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time complexity: O(N)
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        pos = 0
        curNode = head
        while curNode:
            if curNode not in visited:
                visited.add(curNode)
            else:
                return curNode
            curNode = curNode.next
            pos += 1
        return None