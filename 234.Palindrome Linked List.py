# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #Time complexity: O(N)
        #Space complexity: O(1) making changes in-place
        #Two pointers, find midpoint
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Reverse the second part
        cur, last = slow, None
        while cur:
            temp = cur.next
            cur.next = last
            last = cur
            cur = temp
        #Compare the values of two linked list
        p1, p2 = head, last 
        while p2:
            if p1.val != p2.val:
                return False
            p2 = p2.next
            p1 = p1.next
        return True
