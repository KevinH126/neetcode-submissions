class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [] # (dist, [x,y])
        for point in points:
            dist = -1*math.sqrt((point[0])**2 + (point[1])**2)
            heapq.heappush(distances,(dist,point))
            if len(distances) > k:
                heapq.heappop(distances)
        
        output = []
        for i in range(k):
            dist, point = heapq.heappop(distances)
            output.append(point)
        return output