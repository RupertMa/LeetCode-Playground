# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

#A quicker solution:
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp    
        return prev


#Written by Yibo: 
        # if not head:
        #     return None
        # a = ListNode(head.val)
        # head = head.next
        # while head:
        #     b = ListNode(head.val)
        #     b.next = a
        #     a = b
        #     head = head.next
        # return a