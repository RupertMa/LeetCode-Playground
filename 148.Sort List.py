# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity Nlog(N) Space complexity: N
    def sortList(self, head: ListNode) -> ListNode:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        ans = sorted(ans)
        curNode = dummy = ListNode(None)
        while ans:
            curNode.next = ListNode(ans.pop(0))
            curNode = curNode.next
        return dummy.next