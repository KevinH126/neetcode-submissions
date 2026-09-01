class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque() # queue of pending tasks, each have entrance cycle + n, so we check queue[0]'s cycle+n with the curr cycle to see if we push it back to heap
        counts = Counter(tasks)

        heap = []
        for task, count in counts.items():
            heapq.heappush_max(heap,count)
        
        cycle = 0
        while heap or queue:
            cycle+=1
            if heap:
                count = heapq.heappop_max(heap)
                if count > 1:
                    count-=1
                    queue.append((cycle+n,count))
            if queue and queue[0][0] == cycle:
                cyc, count = queue.popleft()
                heapq.heappush_max(heap,count)
        return cycle