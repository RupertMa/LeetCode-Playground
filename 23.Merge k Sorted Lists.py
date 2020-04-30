# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

ListNode.__lt__ = lambda x, y : x.val < y.val

class Solution:
    import heapq
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(None)
        curNode = dummy
        heap = []
        
        for lst in lists:
            if lst:
                heapq.heappush(heap, lst)
                
        while heap:
            head = heapq.heappop(heap)
            curNode.next = head
            curNode = head
            if head.next:
                heapq.heappush(heap, head.next)
                
        return dummy.next
        