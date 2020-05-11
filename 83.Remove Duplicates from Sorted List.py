# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Approach 1: Iterate over the list and return a new list
    # Time complexity: O(N)
    # Space complexity: O(N)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        curNode = dummy
        Set = set()
        while head:
            if head.val not in Set:
                Set.add(head.val)
                curNode.next = ListNode(head.val)
                curNode = curNode.next
            head = head.next
        return dummy.next

    # Approach 2: Edit lined list itself.
    # Time complexity: O(N)
    # Space complexity: O(1)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curNode = head
        while curNode:
            if curNode and curNode.next and curNode.val == curNode.next.val:
                curNode.next = curNode.next.next
            else:
                curNode = curNode.next
        return head