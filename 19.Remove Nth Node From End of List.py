# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = head
        length = 0
        cur = 0
        prev = None
        while fast:
            fast = fast.next
            length += 1
        while length - cur > n:
            prev = slow
            slow = slow.next
            cur += 1
        if prev:
            prev.next = slow.next
        else:
            head = head.next
        return head
