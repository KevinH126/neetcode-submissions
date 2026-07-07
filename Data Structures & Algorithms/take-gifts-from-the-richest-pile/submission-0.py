class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-x for x in gifts]
        heapq.heapify(heap)


        for _ in range(k):
            largest = -heapq.heappop(heap)          # undo negation → real value
            heapq.heappush(heap, -floor(sqrt(largest)))
        
        return -sum(heap)