class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        store = deque()

        j = 0
        for i in range(m+n):
            if i < m:
                store.append(nums1[i])
            
            if store and (j >= n or store[0] <= nums2[j]):
                nums1[i] = store.popleft()
            else:
                nums1[i] = nums2[j]
                j+=1



