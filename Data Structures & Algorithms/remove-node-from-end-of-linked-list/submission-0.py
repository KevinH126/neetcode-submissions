# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        beg = head
        length = 0
        temp = head
        while temp:
            length+=1
            temp = temp.next
        i = length-n

        if i == 0:
            return head.next
        prev, temp = head, head.next
        while i > 1 and temp.next:
            prev = prev.next
            temp = temp.next
            i-=1
        prev.next = temp.next
        return beg