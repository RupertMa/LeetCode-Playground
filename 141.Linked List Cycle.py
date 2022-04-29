# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Time complexity: O(N)
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        pos = 0
        curNode = head
        while curNode:
            if curNode not in visited:
                visited.add(curNode)
            else:
                return True
            curNode = curNode.next
            pos += 1
        return False

    def hasCycle(self, head: ListNode) -> bool:
        cur = head
        seen = set()
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False
