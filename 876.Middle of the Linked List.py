# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        # method1: append to list
        # ans = []
        # while head:
        #     ans.append(head)
        #     head = head.next
        # return ans[len(ans)//2]
        
        # method2: fast and slow traverse
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow