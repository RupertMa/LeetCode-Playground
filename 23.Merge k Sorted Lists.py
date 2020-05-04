# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode.__lt__ = lambda x, y : x.val < y.val

# Method 1: Use heap to sort a list of list node: 
class Solution:
    import heapq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(None)
        curNode = dummy
        lists = [l for l in lists if l]
        heapq.heapify(lists) #Time complexity klog(k)
        
         #Time complexity nlog(k)        
        while lists:
            curNode.next = heapq.heappop(lists)
            curNode = curNode.next
            if curNode.next:
                heapq.heappush(lists, curNode.next)
                
        return dummy.next

# Method 2: Dive and Conquer 
# Time complexity: nlog(k )
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.mergeHelper(lists)
    
    def mergeHelper(self,lists):
        n = len(lists)
        if n == 1:
            return lists[0]
        elif n > 1:
            left = self.mergeHelper(lists[:n//2])
            right = self.mergeHelper(lists[n//2:])
            return self.mergeTwoLists(left,right)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        dummy = ListNode(None)
        curNode = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curNode.next = l1
                l1 = l1.next
            else:
                curNode.next = l2
                l2 = l2.next
            curNode = curNode.next
        curNode.next = l1 or l2
        return dummy.next