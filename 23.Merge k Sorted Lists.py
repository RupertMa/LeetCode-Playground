# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode.__lt__ = lambda x, y : x.val < y.val


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