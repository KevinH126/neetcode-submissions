# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stac1 = []
        stac2 = []

        while l1:
            stac1.append(l1.val)
            l1=l1.next
        while l2:
            stac2.append(l2.val)
            l2=l2.next


        carry = 0
        head = ListNode()
        nxt = None
        i,j = len(stac1)-1,len(stac2)-1
        while i >= 0 and j >= 0:
            added = stac1[i] + stac2[j] + carry
            head.next = ListNode((added%10), nxt)
            carry = added // 10
            nxt = head.next
            i-=1
            j-=1
        while i >= 0:
            val = stac1[i]+carry
            head.next = ListNode(val%10,nxt)
            nxt = head.next
            i-=1
            carry = val//10
        while j >= 0:
            val = stac2[j]+carry
            head.next = ListNode(val%10,nxt)
            nxt = head.next
            j-=1
            carry = val//10
        if carry > 0:
            head.next = ListNode(1,nxt)
        return head.next