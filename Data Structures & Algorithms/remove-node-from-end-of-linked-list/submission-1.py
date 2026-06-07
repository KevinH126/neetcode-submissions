# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        count = 1
        while start:
            start = start.next
            count+=1
        prev = None
        start = head
        for i in range(count-n-1):
            prev = start
            start = start.next
        if prev:
            prev.next = start.next
            return head
        return head.next