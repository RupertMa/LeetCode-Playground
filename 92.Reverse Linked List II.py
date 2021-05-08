# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        length = right - left + 1
        while left-1:
            cur = cur.next
            left -= 1
        prev_left = cur
        cur = cur.next
        stack = []
        while length:
            stack.append(cur)
            cur = cur.next
            length -= 1
        prev_right = cur
        while stack:
            next_node = stack.pop()
            prev_left.next = next_node
            prev_left = prev_left.next
        prev_left.next = prev_right
        return dummy.next

    # Time complexity: O(N)
    # Space complexity: O(N)
