class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1,nums2

        if len(A) > len(B):
            A = nums2
            B = nums1
        
        total = len(A) + len(B)
        half = total//2

        l,r = 0, len(A)-1
        while True:
            m = (l+r)//2
            j = half-(m+1)-1

            aLeft = A[m] if m >= 0 else float("-infinity")
            aRight = A[m+1] if (m+1) < len(A) else float("infinity")
            bLeft = B[j] if j >= 0 else float("-infinity")
            bRight = B[j+1] if (j+1) < len(B) else float("infinity")

            if aLeft > bRight:
                r = m - 1
            elif bLeft > aRight:
                l = m + 1
            else:
                if total % 2 == 1:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft,bLeft) + min(aRight,bRight)) / 2
        return -1


