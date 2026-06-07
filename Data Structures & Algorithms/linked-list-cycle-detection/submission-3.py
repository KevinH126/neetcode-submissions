# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s, d = head, head.next

        while s and d:
            if s == d:
                return True
            s = s.next
            d = d.next
            if not d:
                return False
            else:
                d = d.next
        return False