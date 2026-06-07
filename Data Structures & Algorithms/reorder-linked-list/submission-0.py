class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Fix 1: use separate pointer to count
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        if length <= 2:
            return

        # Fix 2: correct split point for even-length lists
        threshold = (length - 1) // 2
        start = head
        prev, curr = None, head
        i = 0
        while i < length:
            # Fix 3: sever first half and reset prev before reversing
            if i == threshold + 1:
                prev.next = None
                prev = None

            if i > threshold:
                temp = curr.next
                curr.next = prev
                prev = curr
                if temp:
                    curr = temp
            else:
                prev = curr
                curr = curr.next
            i += 1

        # Fix 4: guard against None in merge
        i = 0
        while start and curr and start != curr:
            if i % 2 == 0:
                temp = start.next
                start.next = curr
                start = temp
            else:
                temp = curr.next
                curr.next = start
                curr = temp
            i += 1