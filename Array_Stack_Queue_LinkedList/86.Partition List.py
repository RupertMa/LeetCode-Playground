from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Approach 1:
# Time complexity O(N)
# Space complexity O(N)
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        right_dummy_head = ListNode()
        left_dummy_head = ListNode()
        left = left_dummy_head
        right = right_dummy_head
        while head:
            if head.val >= x:
                right.next = head
                right = right.next
            else:
                left.next = head
                left = left.next
            head = head.next
        left.next = right_dummy_head.next
        # the most important step is to remove the pointer from right node; otherwise memory limit exceeded
        right.next = None
        return left_dummy_head.next