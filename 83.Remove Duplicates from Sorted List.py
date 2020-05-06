# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
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