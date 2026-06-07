# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        s2 = ""

        curr = l1
        while curr:
            s1 = str(curr.val) + s1
            curr = curr.next

        curr = l2
        while curr:
            s2 = str(curr.val) + s2
            curr = curr.next
        
        i1 = int(s1)
        i2 = int(s2)

        ir = i1 + i2
        digit_array = [int(d) for d in str(ir)]
        digit_array.reverse()

        head = ListNode(digit_array[0], None)
        temp = head
        i = 1
        while i < len(digit_array):
            temp.next = ListNode(digit_array[i], None)
            temp = temp.next
            i+=1
        return head